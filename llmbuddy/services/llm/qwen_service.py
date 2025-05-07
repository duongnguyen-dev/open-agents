import os
import asyncio
from dotenv import load_dotenv
from loguru import logger
from langchain_huggingface import HuggingFaceEndpoint
from langchain.callbacks import AsyncIteratorCallbackHandler
from llmbuddy.services.llm.base_service import LLMService
from llmbuddy.services.streaming.streaming_service import StreamlitStreamingService

load_dotenv()

class QwenService(LLMService):
    def __init__(self, model_path):
        super().__init__()
        
        self.streaming = StreamlitStreamingService()
        
        if model_path == None:
            self.llm = HuggingFaceEndpoint(
                repo_id="Qwen/Qwen2.5-Omni-3B",
                task='text-generation',
                max_new_tokens=1024,
                do_sample=False,
                repetition_penalty=1.03,
                huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
                streaming=True
            )
        else:
            logger.error("We haven't support local model yet!")
            self.llm = None
        
    async def generate_text(self, user_input: str):
        # task = asyncio.create_task(self.llm(user_input, callbacks=[self.streaming]))
        # async for token in self.streaming.aiter():
        #     yield token
        # await task
        pass