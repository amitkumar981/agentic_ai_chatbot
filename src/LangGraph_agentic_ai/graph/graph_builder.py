from langgraph.graph import StateGraph,START,END
from src.LangGraph_agentic_ai.nodes.basic_chatbot_node import BasicChatbotNode
from src.LangGraph_agentic_ai.nodes.chatbot_with_tool_node import ChatbotToolNode
from src.LangGraph_agentic_ai.tools.get_tools import get_tools,create_tool_node
from src.LangGraph_agentic_ai.nodes.news_node import News
from langgraph.prebuilt import ToolNode,tools_condition
from src.LangGraph_agentic_ai.state.state import State
class Graph_Builder:
    def __init__(self,model):
        self.llm=model
        self.graph_builder=StateGraph(State)
    
    def basic_chatbot_graph(self):
        'build basic chatbot graph with  Langgraph'
        self.basic_chatbot_node=BasicChatbotNode(self.llm)
        
        #add  node in graph
        self.graph_builder.add_node('chatbot',self.basic_chatbot_node.process)

        #add edge
        self.graph_builder.add_edge(START,'chatbot')
        self.graph_builder.add_edge('chatbot',END)

    def chatbot_with_tools_graph(self):
        "build a chatbot with tool integration"
        
        #define tools
        tools=get_tools()
        tool_node=create_tool_node(tools)

        #define chat_with_tools node
        chatbot_with_tools_obj=ChatbotToolNode(self.llm)
        chatbot_with_tool_node=chatbot_with_tools_obj.create_chatbot(tools)
        
        #add node
        self.graph_builder.add_node('chatbot',chatbot_with_tool_node)
        self.graph_builder.add_node('tools',tool_node)

        #add edges
        self.graph_builder.add_edge(START,'chatbot')
        self.graph_builder.add_conditional_edges('chatbot',tools_condition,
                           {'tools':'tools'}
                           )
        self.graph_builder.add_edge('tools','chatbot')
        self.graph_builder.add_edge('chatbot',END)

    def summerize_news_graph(self):
        news_node=News(self.llm)

        #add node
        self.graph_builder.add_node('fatch_news',News.fatch_news)
        self.graph_builder.add_node('summerize',News.summerize_news)
        self.graph_builder.add_node('save_news',News.save_result)

        #add edge
        self.graph_builder.set_entry_point('fatch_news')
        self.graph_builder.add_edge('fatch_news','summerize')
        self.graph_builder.add_edge('summerize','save_news')
        self.graph_builder.add_edge('save_news',END)
    
    
    def compile_graph(self,usecase:str):
        if usecase=='Basic Chatbot':
            self.basic_chatbot_graph()
        elif usecase=='Chatbot_with_tools':
            self.chatbot_with_tools_graph()
        elif usecase=='News':
            self.summerize_news_graph()
        return self.graph_builder.compile()
    
    


        

