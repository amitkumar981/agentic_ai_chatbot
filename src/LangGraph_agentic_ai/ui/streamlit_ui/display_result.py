import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
import json

class DisplayStreamlitResults:
    def __init__(self, usecase, graph, user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    def results_on_ui(self):
        usecase = self.usecase
        graph = self.graph
        user_message = self.user_message

        if usecase == 'Basic Chatbot':
            # Send HumanMessage as a list
            for event in graph.stream({'messages': [HumanMessage(content=user_message)]}):
                for value in event.values():
                    messages = value.get('messages', [])
                    for msg in messages:
                        if isinstance(msg, HumanMessage):
                            with st.chat_message('user'):
                                st.write(msg.content)
                        elif isinstance(msg, AIMessage):
                            with st.chat_message('assistant'):
                                st.write(msg.content)

        elif usecase == 'Chatbot_with_tools':
            initial_state = {"messages": [HumanMessage(content=user_message)]}
            res = graph.invoke(initial_state)

            for message in res.get('messages', []):
                if isinstance(message, HumanMessage):
                    with st.chat_message("user"):
                        st.write(message.content)
                elif isinstance(message, ToolMessage):
                    with st.chat_message("assistant"):
                        st.write(f"🛠 Tool Response:\n{message.content}")
                elif isinstance(message, AIMessage):
                    with st.chat_message("assistant"):
                        st.write(message.content)


                



