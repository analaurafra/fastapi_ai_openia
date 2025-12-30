# FastAPI + OpenIA 


Aplicação exemplo que expõe uma API HTTP construída com FastAPI para integrar com modelos de linguagem (OpenAI / API compatíveis). O objetivo é fornecer um ponto de partida simples para criar endpoints que geram texto/ respostas usando um serviço de LLM.

> Observação: ajuste exemplos de comandos e nomes de arquivos conforme a estrutura real do seu repositório (por exemplo `main:app`, `app.main:app`, etc.).

![Gif_Swagger](./static/img/screen-capture-_16_.gif)


## Funcionalidades

- Endpoints HTTP com FastAPI para enviar prompts a um modelo de linguagem.
- Suporte para configuração via variáveis de ambiente (.env).
- Exemplo de requisição e resposta JSON.
- Compatível com OpenAI ou outras APIs compatíveis (Azure OpenAI, endpoints customizados).

## Tecnologias

- Python 3.10+
- FastAPI
- Uvicorn (servidor ASGI)
- Requests / httpx (cliente HTTP — dependendo da implementação)
- dotenv (carregamento de variáveis de ambiente)
- (Opcional) Docker

## Pré-requisitos

- Python 3.10+ instalado
- Conta e chave de API do provedor de LLM (por exemplo, OpenAI)
- Git (opcional)

## Instalação (local)

1. Clone o repositório:
```bash
git clone https://github.com/analaurafra/fastapi_ai_openia.git
cd fastapi_ai_openia
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv .venv
# Linux / macOS
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

3. Instale dependências:
```bash
pip install -r requirements.txt
```

4. Crie um arquivo `.env` (ou exporte variáveis no seu ambiente) com as variáveis mínimas:

```env
# Exemplo de variáveis
OPENAI_API_KEY=sk-...
# Caso use endpoint customizado / Azure:
# OPENAI_API_BASE=https://your-azure-openai-endpoint.openai.azure.com/
# OPENAI_API_TYPE=azure
# OPENAI_API_VERSION=2023-10-01
# AZURE_OPENAI_DEPLOYMENT_NAME=deployment-name
```

Ajuste as variáveis conforme a implementação do cliente no projeto.

## Executando a aplicação

Com o ambiente ativo e variáveis configuradas, execute com Uvicorn:

```bash
# ajuste "main:app" para o módulo/objeto correto do seu projeto se necessário
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

A API estará disponível em: http://localhost:8000

A documentação interativa (Swagger UI) estará em: http://localhost:8000/docs  
Redoc: http://localhost:8000/redoc

## Endpoints de exemplo

A estrutura exata dos endpoints pode variar — abaixo estão exemplos comuns que você pode adaptar.

- GET /health
  - Descrição: verifica se a API está no ar.
  - Exemplo:
    ```bash
    curl http://localhost:8000/health
    ```

- POST /generate
  - Descrição: envia um prompt e recebe uma resposta gerada pelo modelo.
  - Body (JSON) de exemplo:
    ```json
    {
      "prompt": "Escreva um resumo curto sobre energia renovável.",
      "model": "gpt-4",
      "max_tokens": 200
    }
    ```
  - Exemplo com curl:
    ```bash
    curl -X POST "http://localhost:8000/generate" \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -d '{"prompt":"Escreva um haicai sobre tecnologia.","model":"gpt-4","max_tokens":60}'
    ```

- POST /chat (exemplo para conversação com histórico)
  - Body (JSON) de exemplo:
    ```json
    {
      "messages": [
        {"role": "system", "content": "Você é um assistente útil."},
        {"role": "user", "content": "Me explique o que é FastAPI."}
      ],
      "model": "gpt-4"
    }
    ```

A resposta típica será um JSON com o texto gerado, metadados e possivelmente a utilização de tokens.

## Exemplo de resposta (exemplo genérico)
```json
{
  "id": "resp_123",
  "object": "text_response",
  "model": "gpt-4",
  "choices": [
    {
      "text": "FastAPI é um framework moderno, rápido (high-performance) para construir APIs com Python 3.7+...",
      "index": 0
    }
  ],
  "usage": {
    "prompt_tokens": 12,
    "completion_tokens": 45,
    "total_tokens": 57
  }
}
```

## Docker (opcional)

Exemplo rápido de como rodar com Docker (supondo que exista um Dockerfile no repositório):

```bash
# build
docker build -t fastapi-ai-openia:latest .

# rodar (expondo porta 8000) — passe variáveis de ambiente
docker run -e OPENAI_API_KEY="${OPENAI_API_KEY}" -p 8000:8000 fastapi-ai-openia:latest
```

## Testes

- Se houver testes, execute:
```bash
pytest
```

## Boas práticas de segurança

- Nunca comite sua chave de API no repositório.
- Use segredos do CI ou um cofre de segredos em vez de variáveis em texto puro quando em produção.
- Configure limites, logging e monitoramento para proteger custos e uso indevido.

## Como contribuir

1. Abra uma issue descrevendo a feature/bug.
2. Crie um branch com um nome descritivo.
3. Faça commits pequenos e claros.
4. Abra um pull request apontando para a branch principal do repositório.

## Licença

Adicione aqui a licença do seu projeto (por exemplo, MIT). Se ainda não definiu, considere adicionar um arquivo LICENSE.

---

Se quiser, eu posso:
- Gerar automaticamente um arquivo README.md pronto para commitar (posso incluir um template de .env).
- Ajustar exemplos de endpoints para refletirem a implementação real (se você me enviar as rotas/handlers do projeto).
- Adicionar badges (build, coverage, license) ao topo do README.

Quer que eu gere o arquivo README.md já em formato pronto para adicionar ao repositório?  


![Thanks](./static/img/thumbs-up-computer.gif)