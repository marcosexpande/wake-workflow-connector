# Wake Workflow Connector

Conector em Python para acionar eventos da plataforma Wake DXP (ex-All iN) a partir de dados de uma lista, com estrutura compatível para orquestração futura em Airflow.

## 📌 Funcionalidades

- Autentica nas APIs da Wake DXP:
  - Geração de token para leitura de listas (segmentação)
  - Geração de token para envio de eventos (workflow transacional)
- Consulta dados de uma lista via API
- Dispara eventos de workflow um a um com os dados da lista
- Compatível com execução local e futura integração com Airflow

## ⚙️ Estrutura do Projeto

```
wake_workflow_connector/
├── .env.example           # Modelo de variáveis de ambiente
├── main.py                # Executa o processo completo (produção)
├── main_mock.py           # Executa com dados simulados (teste)
├── requirements.txt       # Dependências do projeto
├── utils/
│   ├── segment_api.py     # Token e leitura da lista
│   └── workflow_api.py    # Token e envio de evento
```

## 🔧 Como usar

1. Clone este repositório:
```bash
git clone https://github.com/seuusuario/wake-workflow-connector.git
cd wake-workflow-connector
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv .venv
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

5. Execute com mock (teste):
```bash
python main_mock.py
```

6. Execute com dados reais (produção):
```bash
python main.py
```

## 📤 Próximos passos

- Integração com Airflow
- Retry com log de falhas
- Cache de tokens com Redis ou banco

---

Desenvolvido para uso interno por Professional Services - Wake DXP.
