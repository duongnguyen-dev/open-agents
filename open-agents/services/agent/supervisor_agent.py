from langgraph_supervisor import create_supervisor
from langchain_core.messages import HumanMessage
from langgraph.types import Command
from langgraph.graph import StateGraph, MessagesState, START, END
from llmbuddy.services.agent.base_service import AgentService

class SupervisorAgent(AgentService):
    def __init__(self, model, agents):
        super().__init__()
        self.model = model
        self.agents = agents
        
        self.supervisor_agent = create_supervisor(
            model = self.model,
            agents=self.agents, 
            prompt=(
                "You are a supervisor managing two agents:\n"
                "- A weather agent. Assign weather-related tasks to this agent\n"
                "- A web search agent. Assign research-related tasks to this agent\n"
                "Assign work to one agent at a time, do not call agents in parallel.\n"
                "Do not do any work yourself."
            ),
            add_handoff_back_messages=False,
            output_mode="full_history",
            supervisor_name="llmbuddy_supervisor"
        ).compile()
    
    def invoke(self, question: str, *args, **kwargs):
        for token in self.supervisor_agent.stream(
            {"messages": [HumanMessage(content=question)]},
            stream_mode="messages"
        ):
            yield token
        
    async def ainvoke(self, question: str, *args, **kwargs):
        async for token in self.supervisor_agent.astream(
            {"messages": [HumanMessage(content=question)]},
            stream_mode="messages"
        ):  
            yield token