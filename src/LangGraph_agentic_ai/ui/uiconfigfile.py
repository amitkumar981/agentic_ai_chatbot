from configparser import ConfigParser

class config:
    def __init__(self, configfile=r'src\LangGraph_agentic_ai\ui\uiconfigfile.ini'):
        self.Config = ConfigParser()
        self.Config.read(configfile)  

    def get_llm_options(self):
        return self.Config['DEFAULT'].get('LLM_OPTIONS').split(",")

    def get_groq_model_options(self):
        return self.Config['DEFAULT'].get('GROQ_MODEL_OPTIONS').split(",")

    def get_page_title(self):
        return self.Config['DEFAULT'].get('PAGE_TITLE')

    def get_usecase_options(self):
        return self.Config['DEFAULT'].get('USECASE_OPTIONS').split(",")

    
    
    

        