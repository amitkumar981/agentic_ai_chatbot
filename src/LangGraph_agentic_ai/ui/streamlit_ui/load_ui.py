import streamlit as st
import os
from src.LangGraph_agentic_ai.ui.uiconfigfile import config

class LoadStreamlitUI:
    def __init__(self):
        self.config = config()
        self.user_controls = {}

    def load_streamlit_ui(self):
        st.set_page_config(page_title="🤖 " + self.config.get_page_title(), layout="wide")
        st.header("🤖 " + self.config.get_page_title())

        with st.sidebar:
            # Get options from config
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            # LLM selection
            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)

            if self.user_controls["selected_llm"] == 'Groq':
                # Model selection
                model_options = self.config.get_groq_model_options()
                self.user_controls["selected_groq_model"] = st.selectbox("Select Model", model_options)
                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"] = st.text_input("API Key", type="password")
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("⚠️ Please enter your GROQ API key to proceed. Don't have one? Refer: https://console.groq.com/keys")

            # Usecase selection
            self.user_controls["selected_usecase"] = st.selectbox("Select Usecases", usecase_options)

            if self.user_controls['selected_usecase'] in ['Chatbot_with_tools', 'News', 'AI News']:
                self.user_controls['TEVILY_API_KEY'] = st.session_state['TEVILY_API_KEY'] = st.text_input('TEVILY_API_KEY', type='password')
                os.environ['TEVILY_API_KEY'] = self.user_controls['TEVILY_API_KEY']

                if not self.user_controls['TEVILY_API_KEY']:
                    st.warning('⚠️ Please enter your TEVILY_API_KEY.')

            if self.user_controls['selected_usecase'] == "AI News":
                st.subheader("📰 AI News Explorer")
                time_frame = st.selectbox(
                    "📅 Select Time Frame",
                    ["Daily", "Weekly", "Monthly"],
                    index=0
                )

                if st.button("🔍 Fetch Latest AI News", use_container_width=True):
                    st.session_state.IsFetchButtonClicked = True
                    st.session_state.timeframe = time_frame

        return self.user_controls








