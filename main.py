from fastapi import FastAPI,status
from schemas import GenerateRequest,GenerateResponse
from ai_service import generate_text
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="FastAPI + LLM")

@app.post("/ai/generate",
    response_model=GenerateResponse,
    status_code=status.HTTP_200_OK
)
def generate(request: GenerateRequest):
    result = generate_text(request.prompt)
    return {"output": result}
