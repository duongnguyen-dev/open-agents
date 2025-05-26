from pydantic import BaseModel, ConfigDict
from llmbuddy.services.llm.base_service import LLMService

class ChatModel(BaseModel):
    # model_config = ConfigDict(arbitrary_types_allowed=True)
    user_input: str