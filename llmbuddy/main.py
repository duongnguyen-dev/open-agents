from contextlib import asynccontextmanager
from fastapi import FastAPI
from llmbuddy.controllers.llm.llm_controller import router as llm_router
from llmbuddy.controllers.chat.chat_controller import router as chat_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.model = {} 
    app.state.model['llm'] = None
    yield
    app.state.model.clear()

app = FastAPI(lifespan=lifespan)
app.include_router(llm_router, prefix="/llm", tags=["llm"])
app.include_router(chat_router, prefix="/chat", tags=["chat"])