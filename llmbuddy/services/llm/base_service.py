from abc import ABC, abstractmethod

class LLMService(ABC):
    @abstractmethod
    async def generate_text(self):
        pass