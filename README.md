
# Wake Workflow Connector

Conector em Python para acionar eventos da plataforma Wake DXP (ex-All iN) a partir de dados de uma lista de segmentação. Estrutura pronta para integração futura com Airflow.

## 📌 Funcionalidades

- Autentica nas APIs da Wake DXP:
  - Geração de token para leitura de listas (segmentação) via username/password
  - Geração de token para envio de eventos (workflow transacional)
- Consulta dados de uma lista via API com paginação
- Dispara eventos de workflow com dados personalizados (email, celular, nome)
- Compatível com execução local e futura orquestração via Airflow

## ⚙️ Estrutura do Projeto

```
wake_workflow_connector/
├── .env.example           # Modelo de variáveis de ambiente
├── main.py                # Executa o processo completo (produção)
├── main_mock.py           # Executa com dados simulados (teste)
├── requirements.txt       # Dependências do projeto
├── utils/
│   ├── segment_api.py     # Token dinâmico + leitura de lista segmentada
│   └── workflow_api.py    # Token + envio de evento transacional
```

## 🔧 Como usar

1. Clone este repositório:
```bash
git clone https://github.com/seuusuario/wake-workflow-connector.git
cd wake-workflow-connector
```

2. Crie e ative um ambiente virtual:
```bash
python3 -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate   # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Copie o arquivo `.env.example` e crie o `.env` com seus dados reais:
```bash
cp .env.example .env
```

5. Execute com dados reais (produção):
```bash
python3 main.py
```

## 🌐 Variáveis de Ambiente (.env)

```env
SEGMENT_USERNAME=seu_usuario
SEGMENT_PASSWORD=sua_senha
WORKFLOW_USERNAME=seu_usuario_workflow
WORKFLOW_PASSWORD=sua_senha_workflow
LIST_ID=1234567
```

## 🧠 Comportamento inteligente

- Tokens são armazenados localmente com controle de validade (12h)
- Fluxo automatizado para:
  - Autenticar
  - Ler usuários da lista
  - Acionar evento de workflow
- Compatível com orquestração (Airflow)

## 📤 Próximos passos

- Integração com Airflow
- Retry e tratamento de falhas com log persistente
- Melhorias na interface de logs e relatórios

---

Desenvolvido para uso interno por Professional Services - Wake DXP.
Atualizado em: Maio/2025
