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
        
        elif usecase == "News":
            frequency = self.user_message
            with st.spinner("Fetching and summarizing news... ⏳"):
                result = graph.invoke({"messages": frequency})
                try:
                    # Read the markdown file
                    AI_NEWS_PATH = f"./News/{frequency.lower()}_summary.md"
                    with open(AI_NEWS_PATH, "r") as file:
                        markdown_content = file.read()

                    # Display the markdown content in Streamlit
                    st.markdown(markdown_content, unsafe_allow_html=True)
                except FileNotFoundError:
                    st.error(f"News Not Generated or File not found: {AI_NEWS_PATH}")
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")


                



