from abc import ABC, abstractmethod

class AgentService(ABC):
    @abstractmethod
    def invoke(self, question: str, *args, **kwargs):
        pass