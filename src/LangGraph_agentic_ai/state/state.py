#importing libraies
from typing_extensions import TypedDict,List
from langgraph.graph.message import add_messages
from typing import Annotated

#define class
class State(TypedDict):
    """class represents the state of the input to assistant"""
    messages:Annotated[List,add_messages]  


