
import os
import requests
import json
from datetime import datetime, timedelta

TOKEN_FILE = "segment_token.json"

def is_token_valid(token_data):
    expires_at = datetime.fromisoformat(token_data["expires_at"])
    return datetime.utcnow() < expires_at

def load_cached_token():
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, "r") as f:
            try:
                token_data = json.load(f)
                if is_token_valid(token_data):
                    return token_data["access_token"]
            except Exception:
                return None
    return None

def get_segment_token():
    cached_token = load_cached_token()
    if cached_token:
        return cached_token

    username = os.getenv("SEGMENT_USERNAME")
    password = os.getenv("SEGMENT_PASSWORD")

    url = "https://painel02.allinmail.com.br/allinapi/?method=get_token"
    headers = {
        "accept": "application/json",
        "content-type": "application/x-www-form-urlencoded"
    }
    data = {
        "username": username,
        "password": password
    }

    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()
    access_token = response.json()["token"]

    token_data = {
        "access_token": access_token,
        "expires_at": (datetime.utcnow() + timedelta(hours=11, minutes=30)).isoformat()
    }

    with open(TOKEN_FILE, "w") as f:
        json.dump(token_data, f)

    return access_token

def get_list_users(token, list_id, limit=100):
    all_users = []
    page = 1

    while True:
        url = f"https://segments-xp.wake.tech/v1/lists/{list_id}?limit={limit}&page={page}"
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
        page += 1

    return all_users
