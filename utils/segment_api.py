import os
import requests
import json
from datetime import datetime, timedelta

# Caminho local para armazenar o token gerado
TOKEN_FILE = "segment_token.json"

# Função para verificar se o token armazenado ainda é válido
def is_token_valid(token_data):
    expires_at = datetime.fromisoformat(token_data["expires_at"])
    return datetime.utcnow() < expires_at

# Geração ou reutilização do token com cache
def get_segment_token():
    # Verifica se já existe token salvo localmente
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, "r") as f:
            token_data = json.load(f)
            if is_token_valid(token_data):
                return token_data["access_token"]

    # Se não existir ou estiver expirado, gera novo token
    url = "https://painel02.allinmail.com.br/allinapi/?method=get_token"
    payload = {
        "username": os.getenv("SEGMENT_USERNAME"),
        "password": os.getenv("SEGMENT_PASSWORD")
    }
    response = requests.post(url, json=payload)
    response.raise_for_status()
    access_token = response.json()["access_token"]

    # Salva token com tempo de expiração (12h - margem de 30min)
    token_data = {
        "access_token": access_token,
        "expires_at": (datetime.utcnow() + timedelta(hours=11, minutes=30)).isoformat()
    }

    with open(TOKEN_FILE, "w") as f:
        json.dump(token_data, f)

    return access_token

# Busca lista de usuários com base no ID
def get_list_users(token, list_id, limit=100):
    all_users = []
    offset = 0

    while True:
        url = f"https://segments-xp.wake.tech/v1/lists/{list_id}?limit={limit}&offset={offset}"
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()
        result = response.json().get("result", [])

        if not result:
            break

        all_users.extend(result)
        offset += limit

    return all_users
