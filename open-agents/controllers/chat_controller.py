from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import StreamingResponse
from langchain_core.messages import ToolMessage
from llmbuddy.models.chat_model import ChatModel

router = APIRouter()

@router.post("/chat_with_llm")
def chat_with_llm(chat_request: ChatModel, request: Request): 
    user_input = chat_request.user_input
    if not user_input: 
        raise HTTPException(status_code=400, detail="Message cannot be empty")

    async def token_generator():
        async for token in request.app.state.model['llm'].generate_text(user_input):
            yield token

    return StreamingResponse(token_generator(), media_type="text/plain")

@router.post("/chat_with_multi_agent")
def chat_with_multi_agent(chat_request: ChatModel, request: Request):
    user_input = chat_request.user_input
    if not user_input: 
        raise HTTPException(status_code=400, detail="Message cannot be empty")

    async def token_generator():
        async for token in request.app.state.model['agent'].ainvoke(user_input):
            if token[0].content == "" or isinstance(token[0], ToolMessage):
                continue
            else:
                yield token[0].content

    return StreamingResponse(token_generator(), media_type="text/plain")

