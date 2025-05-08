from contextlib import asynccontextmanager
from loguru import logger
from fastapi import FastAPI
from llmbuddy.controllers.llm.llm_controller import router as llm_router
from llmbuddy.controllers.chat.chat_controller import router as chat_router
from llmbuddy.controllers.documents.documents_controller import router as document_router
from llmbuddy.services.llm.phi4_service import Phi4Service

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.model = {} 
    app.state.model['llm'] = Phi4Service(model_path=None)
    logger.info("Load model successfully")
    yield
    app.state.model.clear()

app = FastAPI(lifespan=lifespan)
app.include_router(llm_router, prefix="/llm", tags=["llm"])
app.include_router(chat_router, prefix="/chat", tags=["chat"])
app.include_router(document_router, prefix="/document", tags=["document"])