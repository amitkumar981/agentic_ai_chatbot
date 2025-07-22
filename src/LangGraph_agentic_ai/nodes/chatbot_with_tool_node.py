from src.LangGraph_agentic_ai.state.state import state

class ChatbotToolNode:
    def __init__(self,model):
        self.llm=model

    def process(self,state):
        "process the input state and generate the response of llm"
        user_input=state['messages'][-1]

        llm_response=self.llm.invoke({'role':'user','content':user_input})

        tool_response={
            'role':'tools',
            'content':f"simulated tool response for : {user_input}"
        }

        return {"messages":[llm_response,tool_response]}
    
    def create_chatbot(self,tools):
        
        #bind with tool
        llm_with_tool=self.llm.bind_tools(tools)

        def chatbot_node(state:state):
            "chatbot logic to process the input and gennerate the response "
            return {"messages":[llm_with_tool.invoke(state['messages'])]}
        return chatbot_node


    
