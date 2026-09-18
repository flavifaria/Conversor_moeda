import requests

def pegar_conversoes(moeda_base):
    url = f"https://api.exchangerate-api.com/v4/latest/{moeda_base}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()["rates"]
    except (requests.RequestException, ValueError, KeyError):
        return None
