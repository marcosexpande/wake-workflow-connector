import os
from dotenv import load_dotenv
from utils.segment_api import get_segment_token, get_list_users
from utils.workflow_api import get_workflow_token, trigger_workflow

# Carrega variáveis do .env
load_dotenv()

LIST_ID = os.getenv("LIST_ID")
WORKFLOW_EVENT = os.getenv("WORKFLOW_EVENT")

print("[DEBUG] LIST_ID carregado do .env:", os.getenv("LIST_ID"))

def main():
    # Autenticação das duas APIs
    segment_token = get_segment_token()
    workflow_token = get_workflow_token()

    # Busca os usuários da lista informada
    users = get_list_users(segment_token, LIST_ID)

    for user in users:
        email = user.get("email")
        phone = user.get("phone")
        full_name = user.get("nome_completo")

        if not email or not phone:
            print(f"[ERRO] Usuário sem e-mail ou telefone: {user}")
            continue

        try:
            resp = trigger_workflow(workflow_token, email, phone, full_name, WORKFLOW_EVENT)
            print(f"[OK] Workflow iniciado para {email}: {resp}")
        except Exception as e:
            print(f"[FALHA] Erro ao processar {email}: {e}")

if __name__ == "__main__":
    main()
