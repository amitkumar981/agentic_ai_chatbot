
from src.LangGraph_agentic_ai.state.state import state


class BasicChatbotNode:
    "implimenting basic chatbot"

    def __init__(self,model):
        self.llm=model
    
    def process(self):
       "process the input and generate the llm response"
       return {"messages":self.llm.invoke(state['messages'])}
    
        
