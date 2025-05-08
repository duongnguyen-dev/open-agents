from fastapi import Request
from fastapi.routing import APIRouter
from llmbuddy.models.llm_model import LLMModel
from llmbuddy.services.llm.phi4_service import Phi4Service

router = APIRouter()

@router.post("/load_llm")
def load_llm(chat_request: LLMModel, request: Request):
    if chat_request.llm_name == "Qwen/Qwen2.5-Omni-3B":
        request.app.state.model['llm'] = Phi4Service(model_path=None)
        print(request.app.state.model['llm'])
        return {"response" : "Model loaded successfully!"}
    return {"response": "Model was not fully loaded!"}
    