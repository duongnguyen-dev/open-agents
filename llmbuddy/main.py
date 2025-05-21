import uvicorn
from contextlib import asynccontextmanager
from loguru import logger
from fastapi import FastAPI
from llmbuddy.controllers.models.models_controller import router as models_router
from llmbuddy.controllers.chat.chat_controller import router as chat_router
from llmbuddy.controllers.documents.documents_controller import router as document_router
from llmbuddy.services.llm.gemini_service import GeminiService
from llmbuddy.services.agent.supervisor_agent import SupervisorAgent
from llmbuddy.services.agent.weather_agent import WeatherAgent

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Init LLM
    app.state.var = {}
    app.state.var['llm'] = GeminiService(model_name="gemini-2.0-flash")
    try:
        app.state.var['agent'] = SupervisorAgent(
            model=app.state.var['llm'],
            agents=[
                WeatherAgent(app.state.var['llm'])(), 
            ]
        )
        logger.info("Load model successfully!")
    except: 
        logger.error("Unable to load model!")
    
    yield
    app.state.var.clear()

app = FastAPI(lifespan=lifespan)

app.include_router(models_router, prefix="/models", tags=["models"])
app.include_router(chat_router, prefix="/chat", tags=["chat"])
app.include_router(document_router, prefix="/document", tags=["document"])

if __name__ == "__main__":
    uvicorn.run("llmbuddy.main:app", host="127.0.0.1", port=8002, reload=True)