from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage
from llmbuddy.tools.weather_tools import FetchCurrentWeatherDataFromCityNameTool
from llmbuddy.services.agent.base_service import AgentService

class WeatherAgent(AgentService):
    def __init__(self, model):        
        self.model = model
        self.tools = [
            FetchCurrentWeatherDataFromCityNameTool()
        ]
        self.name = "weather_agent"
        
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
        
        return response['content']
    
    def __call__(self):
        return self.agent_executor