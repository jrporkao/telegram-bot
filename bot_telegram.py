import requests
import os

# As variáveis TOKEN e CHAT_ID virão dos "Secrets" do GitHub
TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def enviar_mensagem():
    mensagem = "🔥 Nova promoção automática! [Clique aqui](https://meulinkdeafiliado.com)"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    params = {"chat_id": CHAT_ID, "text": mensagem, "parse_mode": "Markdown"}
    requests.get(url, params=params)
    print("Mensagem enviada com sucesso!")

if __name__ == "__main__":
    enviar_mensagem()
