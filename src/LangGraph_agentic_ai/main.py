import streamlit as st
import os
from src.LangGraph_agentic_ai.ui.streamlit_ui.load_ui import LoadStreamlitUI

def load_app():

    #load ui
    ui=LoadStreamlitUI()
    user_input=ui.load_streamlit_ui()
    
    if not user_input:
        st.error("Error : Failed to load userinput from ui")
        return 
    user_massage=st.chat_input('"Enter your message :')
