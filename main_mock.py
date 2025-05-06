from utils.workflow_api import get_workflow_token, trigger_workflow

# --- Mock de dados da lista ---
users = [
    {
        "email": "marcosexpande@gmail.com",
        "phone": "5511999999999",
        "nome_completo": "Marcos Souza Wake"
    }
]

# Gera o token da API de workflow (transacional)
workflow_token = get_workflow_token()

# Nome do evento (pode deixar fixo ou puxar do .env)
WORKFLOW_EVENT = "LembreteUC_Autoinstrucional"

# Loop de envio individual
for user in users:
    email = user["email"]
    phone = user["phone"]
    nome = user["nome_completo"]

    try:
        resp = trigger_workflow(workflow_token, email, phone, nome, WORKFLOW_EVENT)
        print(f"[OK] Workflow enviado para {email}: {resp}")
    except Exception as e:
        print(f"[ERRO] ao processar {email}: {e}")
