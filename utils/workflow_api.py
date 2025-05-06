import os
import requests
import json
from datetime import datetime, timedelta

# Caminho local do cache do token
TOKEN_FILE = "workflow_token.json"

# Verifica validade do token armazenado
def is_token_valid(token_data):
    expires_at = datetime.fromisoformat(token_data["expires_at"])
    return datetime.utcnow() < expires_at

# Gera novo token ou reutiliza existente
def get_workflow_token():
    username = os.getenv("WORKFLOW_USERNAME")
    password = os.getenv("WORKFLOW_PASSWORD")

    # Monta a URL com os parâmetros na própria query string
    url = (
        "https://transacional.allin.com.br/api/"
        f"?username={username}&password={password}&method=get_token&output=json"
    )

    response = requests.get(url)
    response.raise_for_status()

    access_token = response.json()["token"]

    # Salva token com tempo de expiração com margem de segurança (11h30)
    token_data = {
        "access_token": access_token,
        "expires_at": (datetime.utcnow() + timedelta(hours=11, minutes=30)).isoformat()
    }

    with open(TOKEN_FILE, "w") as f:
        json.dump(token_data, f)

    return access_token

# Aciona evento de workflow via API
def trigger_workflow(token, email, phone, full_name, event):
    import json
    url = f"https://transacional.allin.com.br/api/?method=workflow&token={token}"

    # Monta os dados como string JSON embutida (formato exigido)
    payload_json = json.dumps({
        "evento": event,
        "nm_email": email,
        "nm_celular": phone,
        "vars": {
            "nome_completo": full_name
        }
    })

    # Envia como campo 'dados' via multipart/form-data
    files = {
        "dados": (None, payload_json)
    }

    print("[DEBUG] URL:", url)
    print("[DEBUG] Payload JSON:", payload_json)

    response = requests.post(url, files=files)

    print("[DEBUG] Status:", response.status_code)
    print("[DEBUG] Body:", response.text)

    response.raise_for_status()

    try:
        return response.json()
    except ValueError:
        return {"resposta": response.text}



