from pydantic import BaseModel, Field

class GenerateRequest(BaseModel):
    prompt: str = Field(..., example="Explique o FastAPI em poucas Palvras")

class GenerateResponse(BaseModel):
    output: str
