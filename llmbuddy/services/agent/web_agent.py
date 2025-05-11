import os
from langchain_tavily import TavilySearch
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage

from llmbuddy.services.agent.base_service import AgentService

os.environ.get("TAVILY_API_KEY")

class WebAgent(AgentService):
    def __init__(self, model):
        self.model = model
        self.tools = [
            TavilySearch(max_results=5)
        ]
        self.name = "web_agent"
        
        self.agent_executor = create_react_agent(
            model=self.model, 
            tools=self.tools,
            prompt="",
            name=self.name
        )
    
    def invoke(self, question: str, *args, **kwargs):
        response = self.agent_executor.invoke(
            {"messages": [HumanMessage(content=question)]},
            stream_mode="messages"
        )
        
        return response['results']
    
    def __call__(self):
        return self.agent_executor