import streamlit as st
from src.LangGraph_agentic_ai.ui.streamlit_ui.load_ui import LoadStreamlitUI
from src.LangGraph_agentic_ai.LLMS.groq_llm import GROQ_LLM
from src.LangGraph_agentic_ai.graph.graph_builder import graph_builder
from src.LangGraph_agentic_ai.ui.streamlit_ui.display_result import DisplayStreamlitResults

def load_app():
    # Load UI
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("❌ Error: Failed to load user input from UI")
        return

    user_message = st.chat_input("💬 Enter your message:")
    
    if user_message:
        try:
            # Load LLM
            obj_llm_config = GROQ_LLM(user_input)
            model = obj_llm_config.get_llm()

            if not model:
                st.error("❌ Error: Model not initialized")
                return

            # Load usecase
            usecase = user_input.get('selected_usecase')
            if not usecase:
                st.error("❌ Error: Usecase not selected")
                return

            # Build and compile the graph
            builder = graph_builder(model)
            graph = builder.compile_graph(usecase)

            # Display result on UI
            DisplayStreamlitResults(usecase, graph, user_message).results_on_ui()

        except Exception as e:
            st.error(f"🚨 Error while running app: {str(e)}")










