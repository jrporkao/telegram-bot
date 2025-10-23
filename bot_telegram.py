import requests
import os

# Variáveis do ambiente (serão definidas no GitHub)
TOKEN = os.getenv("8475969808:AAG180yzsb2Nzv0jQwH7WXrK-Khgc1n7pp0")
CHAT_ID = os.getenv("1003166982954")

def enviar_mensagem():
    mensagem = "🔥 Nova promoção automática! [Clique aqui](https://meulinkdeafiliado.com)"
    url = f"https://api.telegram.org/bot{8475969808:AAG180yzsb2Nzv0jQwH7WXrK-Khgc1n7pp0}/sendMessage"
    params = {"chat_id": 1003166982954, "text": mensagem, "parse_mode": "Markdown"}
    requests.get(url, params=params)
    print("Mensagem enviada com sucesso!")

if __name__ == "__main__":
    enviar_mensagem()
