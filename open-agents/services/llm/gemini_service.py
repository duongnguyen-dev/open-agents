from dotenv import load_dotenv
from loguru import logger
from langchain_google_genai import ChatGoogleGenerativeAI
from llmbuddy.services.llm.base_service import LLMService

load_dotenv()

class GeminiService(LLMService):
    def __init__(self, model_name):
        super().__init__()
        try:
            self.llm = ChatGoogleGenerativeAI(
                model=model_name,
                temperature=0.7,
                max_tokens=None,
                timeout=None,
                max_retries=2,
            )
            logger.info("Load model successfully!")
        except: 
            logger.error("Failed to load model!")
        
    async def generate_text(self, question: str):
        async for chunk in self.llm.astream(question):
            yield chunk.content
            
    def bind_tools(self, tools):
        return self.llm.bind_tools(tools)