from pydantic import BaseModel

class LLMModel(BaseModel):
    llm_name: str