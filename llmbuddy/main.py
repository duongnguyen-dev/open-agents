from contextlib import asynccontextmanager
from loguru import logger
from fastapi import FastAPI
from llmbuddy.controllers.llm.llm_controller import router as llm_router
from llmbuddy.controllers.chat.chat_controller import router as chat_router
from llmbuddy.controllers.documents.documents_controller import router as document_router
from llmbuddy.services.llm.gemini_service import GeminiService
from llmbuddy.services.agent.supervisor_agent import SupervisorAgent
from llmbuddy.services.agent.weather_agent import WeatherAgent
from llmbuddy.services.agent.web_agent import WebAgent

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.model = {} 
    app.state.model['llm'] = GeminiService(model_name="gemini-2.0-flash")
    app.state.model['agent'] = SupervisorAgent(
        model=app.state.model['llm'],
        agents=[
            WeatherAgent(app.state.model['llm'])(), WebAgent(app.state.model['llm'])()
        ]
    )
    logger.info("Load model successfully")
    yield
    app.state.model.clear()

app = FastAPI(lifespan=lifespan)
app.include_router(llm_router, prefix="/llm", tags=["llm"])
app.include_router(chat_router, prefix="/chat", tags=["chat"])
app.include_router(document_router, prefix="/document", tags=["document"])