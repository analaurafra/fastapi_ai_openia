# FastAPI + OpenIA

Example application that exposes an HTTP API built with FastAPI to integrate with language models (OpenAI / compatible APIs). The goal is to provide a simple starting point for creating endpoints that generate text/responses using an LLM service.

> Note: adjust example commands and file names according to the actual structure of your repository (for example `main:app`, `app.main:app`, etc.).

![Gif_Swagger](./static/img/screen-capture-_16_.gif)

## Features

- HTTP endpoints with FastAPI to send prompts to a language model.
- Support for configuration via environment variables (.env).
- Example JSON request and response.
- Compatible with OpenAI or other compatible APIs (Azure OpenAI, custom endpoints).

## Technologies

- Python 3.10+
- FastAPI
- Uvicorn (ASGI server)
- Requests / httpx (HTTP client — depending on the implementation)
- dotenv (environment variable loading)
- (Optional) Docker

## Prerequisites

- Python 3.10+ installed
- Account and API key from an LLM provider (for example, OpenAI)
- Git (optional)

## Installation (local)

1. Clone the repository:
```bash
git clone https://github.com/analaurafra/fastapi_ai_openia.git
cd fastapi_ai_openia
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
# Linux / macOS
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file (or export variables in your environment) with at least the following variables:
```env
# Example variables
OPENAI_API_KEY=sk-...
# If you use a custom endpoint or Azure:
# OPENAI_API_BASE=https://your-azure-openai-endpoint.openai.azure.com/
# OPENAI_API_TYPE=azure
# OPENAI_API_VERSION=2023-10-01
# AZURE_OPENAI_DEPLOYMENT_NAME=deployment-name
```

Adjust these variables according to the client implementation in the project.

## Running the application

With the virtual environment active and environment variables set, run with Uvicorn:

```bash
# adjust "main:app" to the correct module/object for your project if necessary
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at: http://localhost:8000

Interactive API docs (Swagger UI): http://localhost:8000/docs  
Redoc: http://localhost:8000/redoc

## Example endpoints

The exact endpoint structure may vary — below are common examples you can adapt.

- GET /health  
  - Description: Check if the API is running.
  - Example:
    ```bash
    curl http://localhost:8000/health
    ```

- POST /generate  
  - Description: Send a prompt and receive a generated response from the model.
  - Sample request body (JSON):
    ```json
    {
      "prompt": "Write a short summary about renewable energy.",
      "model": "gpt-4",
      "max_tokens": 200
    }
    ```
  - Curl example:
    ```bash
    curl -X POST "http://localhost:8000/generate" \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -d '{"prompt":"Write a haiku about technology.","model":"gpt-4","max_tokens":60}'
    ```

- POST /chat (example for conversational flows with context)  
  - Sample request body (JSON):
    ```json
    {
      "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain what FastAPI is."}
      ],
      "model": "gpt-4"
    }
    ```

Typical responses are JSON objects containing the generated text, metadata, and possibly token usage.

## Sample response (generic example)
```json
{
  "id": "resp_123",
  "object": "text_response",
  "model": "gpt-4",
  "choices": [
    {
      "text": "FastAPI is a modern, high-performance web framework for building APIs with Python 3.7+...",
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

## Docker (optional)

Quick example of running with Docker (assuming a Dockerfile exists in the repository):

```bash
# build
docker build -t fastapi-ai-openia:latest .

# run (expose port 8000) — pass environment variables
docker run -e OPENAI_API_KEY="${OPENAI_API_KEY}" -p 8000:8000 fastapi-ai-openia:latest
```

## Tests

- If tests exist, run:
```bash
pytest
```

## Security best practices

- Never commit your API key to the repository.
- Use CI secrets or a secret vault instead of plaintext environment variables for production.
- Configure rate limits, logging, and monitoring to protect against misuse and unexpected costs.

## Contributing

1. Open an issue describing the feature or bug.
2. Create a branch with a descriptive name.
3. Make small, focused commits.
4. Open a pull request targeting the repository’s main branch.

## License

Add your project license here (for example, MIT). If you haven't chosen one yet, consider adding a LICENSE file.

![Thanks](./static/img/thumbs-up-computer.gif)
