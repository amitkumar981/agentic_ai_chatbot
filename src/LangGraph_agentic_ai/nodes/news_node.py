from tavily import TavilyClient
from langchain_core.prompts import ChatPromptTemplate

class News:
    def __init__(self,llm):
        self.llm=llm
        self.tavily=TavilyClient()
        self.state={}
    
    #define a method to fatch news
    def fatch_news(self,state:dict) -> dict:
        #get the frequency of state
        frequency=state['messages'][0].lower()

        #store the frquency in state dict
        self.state['frequency']=frequency

        #may the frequrency in tevily keywords
        time_range_map={'daily':'d','weeky':'w','monthly':'m','yearly':'y'}
        days_map={'daily':1,'weekly':7,'monthly':7,'yearly':7}

        #get the response from tavily search
        response = self.tavily.search(
            query="Top Artificial Intelligence (AI) technology news India and globally",
            topic="news",
            time_range=time_range_map[frequency],
            include_answer="advanced",
            max_results=20,
            days=days_map[frequency]
        )

        #pass to the state
        state['news_data']=response.get('results',[])

        #pass to class level state
        self.state['news_data']=state['news_data']

        return state
    
    #define a fuction to summerize 
    def summerize_news(self,state:dict) :

        #get the news data
        news_items=self.state['news_data']

        #Creates a prompt template using LangChain to instruct the LLM to summarize the articles into a specific markdown format
        prompt_template = ChatPromptTemplate.from_messages([
            ("system", """Summarize AI news articles into markdown format. For each item include:
            - Date in **YYYY-MM-DD** format in IST timezone
            - Concise sentences summary from latest news
            - Sort news by date wise (latest first)
            - Source URL as link
            Use format:
            ### [Date]
            - [Summary](URL)"""),
            ("user", "Articles:\n{articles}")
        ])

        #Prepares a single string combining content, URL, and date from each news article
        articles_str = "\n\n".join([
            f"Content: {item.get('content', '')}\nURL: {item.get('url', '')}\nDate: {item.get('published_date', '')}"
            for item in news_items
        ])
        
        #Invokes the LLM with the filled-in prompt (i.e., asking it to summarize the articles)
        response = self.llm.invoke(prompt_template.format(articles=articles_str))

        #Stores the LLM-generated summary in the passed-in state
        state['summary'] = response.content

        #Also stores it in the internal state
        self.state['summary']=state['summary']

        return self.state
    
    #save the results
    def save_result(self,state):
        frequency = self.state['frequency']
        summary = self.state['summary']
        filename = f"./AINews/{frequency}_summary.md"
        with open(filename, 'w') as f:
            f.write(f"# {frequency.capitalize()} AI News Summary\n\n")
            f.write(summary)
        self.state['filename'] = filename
        return self.state



    

