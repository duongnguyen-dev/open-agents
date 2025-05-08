from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import StreamingResponse
from llmbuddy.models.chat_model import ChatModel

router = APIRouter()

@router.post("/generate")
def generate(chat_request: ChatModel, request: Request): 
    user_input = chat_request.user_input
    if not user_input: 
        raise HTTPException(status_code=400, detail="Message cannot be empty")

    async def token_generator():
        async for token in request.app.state.model['llm'].generate_text(user_input):
            yield token

    return StreamingResponse(token_generator(), media_type="text/plain")