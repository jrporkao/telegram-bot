import os
import re
import requests
import time

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")  # opcional, só se precisar enviar pra um chat fixo
URL_BASE = f"https://api.telegram.org/bot{TOKEN}"

PADRAO_LINK = r"(https?://[^\s]+)"

def enviar_mensagem(chat_id, texto, link=None):
    mensagem = f"🔥 *Nova Oferta Encontrada!*\n\n{texto}"
    reply_markup = None
    if link:
        reply_markup = {"inline_keyboard": [[{"text": "🛒 Comprar Agora", "url": link}]]}
    data = {
        "chat_id": chat_id,
        "text": mensagem,
        "parse_mode": "Markdown",
        "reply_markup": reply_markup
    }
    requests.post(f"{URL_BASE}/sendMessage", json=data)

def tratar_mensagem(mensagem):
    chat_id = mensagem["chat"]["id"]
    texto = mensagem.get("text", "") or mensagem.get("caption", "")
    links = re.findall(PADRAO_LINK, texto)
    if links:
        for link in links:
            enviar_mensagem(chat_id, f"Link recebido: {link}", link)

def escutar():
    print("🤖 Bot rodando... aguardando mensagens...")
    ultimo_update = None
    while True:
        try:
            params = {"offset": ultimo_update, "timeout": 30}
            resposta = requests.get(f"{URL_BASE}/getUpdates", params=params, timeout=60).json()
            if "result" in resposta:
                for item in resposta["result"]:
                    ultimo_update = item["update_id"] + 1
                    if "message" in item:
                        tratar_mensagem(item["message"])
        except Exception as e:
            print("Erro no loop:", e)
            time.sleep(5)

if __name__ == "__main__":
    escutar()
