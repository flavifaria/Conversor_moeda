import requests

requisicao = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRLT")

def pegar_conversoes():
    if requisicao.status_code == 200:
        conversao = requisicao.json()
        return conversao
    else:
        return None
