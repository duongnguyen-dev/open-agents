from fastapi import Request
from fastapi.routing import APIRouter
from llmbuddy.models.llm_model import LLMModel
from llmbuddy.services.llm.phi4_service import Phi4Service
from llmbuddy.services.llm.gemini_service import GeminiService

router = APIRouter()

@router.post("/load_llm")
def load_llm(chat_request: LLMModel, request: Request):
    if chat_request.llm_name == "microsoft/Phi-4-mini-reasoning":
        request.app.state.model['llm'] = Phi4Service(model_path=None)
        return {"response" : "Model loaded successfully!"}
    elif chat_request.llm_name == "gemini-2.0-flash":
        request.app.state.model['llm'] = GeminiService(model_name=chat_request.llm_name)
        return {"response" : "Model loaded successfully!"}
    return {"response": "Model was not fully loaded!"}
    