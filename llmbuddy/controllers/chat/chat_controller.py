import asyncio
from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import StreamingResponse
from llmbuddy.models.chat_model import ChatModel
from langchain.callbacks import AsyncIteratorCallbackHandler

router = APIRouter()

@router.post("/generate")
async def generate(chat_request: ChatModel, request: Request): 
    user_input = chat_request.user_input
    if not user_input: 
        raise HTTPException(status_code=400, detail="Message cannot be empty")
    
    model = request.app.state.model['llm']
    callback = AsyncIteratorCallbackHandler()


    # Define an async generator that yields bytes
    async def token_generator():
        task = asyncio.create_task(model.llm(user_input, callbacks=[callback]))
        async for token in callback.aiter():
            yield token.encode('utf-8')
        await task

    return StreamingResponse(token_generator(), media_type="text/plain")