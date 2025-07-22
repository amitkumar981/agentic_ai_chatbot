from langchain_community.tools import TavilySearchResults
from langgraph.prebuilt import ToolNode

def get_tools():
    "returns the list of tools"
    tools=[TavilySearchResults(max_results=3)]
    return tools

def create_tool_node(tools):
    "create a tool node got graph"
    return ToolNode(tools)
