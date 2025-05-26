from fastapi import Request, Depends
from fastapi.routing import APIRouter
from sqlmodel import Session
from llmbuddy.models.llm_model import LLMModel
from llmbuddy.services.llm.phi4_service import Phi4Service
from llmbuddy.services.llm.gemini_service import GeminiService
from llmbuddy.services.models.model_service import ModelService
from llmbuddy.deps import get_session

router = APIRouter()

@router.post("/load_llm")
def load_llm(chat_request: LLMModel, request: Request):
    if chat_request.llm_name == "microsoft/Phi-4-mini-reasoning":
        request.app.state.var['llm'] = Phi4Service(model_path=None)
        return {"response" : "Model loaded successfully!"}
    elif chat_request.llm_name == "gemini-2.0-flash":
        request.app.state.var['llm'] = GeminiService(model_name=chat_request.llm_name)
        return {"response" : "Model loaded successfully!"}
    return {"response": "Model was not fully loaded!"}

@router.get("/")
def list_models(request: Request, session: Session = Depends(get_session)):
    model_service = ModelService(session)
    models = model_service.list_models()

    return {"response": models}
