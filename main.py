from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent
from tools import web_search_tool, wiki_tool, math_tool, llm_tool

from config import OPENAI_API_KEY
chat = ChatOpenAI(openai_api_key=OPENAI_API_KEY)

tools = [web_search_tool, wiki_tool, math_tool, llm_tool]

agent = initialize_agent(
    agent="zero-shot-react-description",
    tools=tools,
    llm=chat,
    verbose=True,
    max_iterations=5
)
while True:
    query = input("Enter a query: ")
    answer = agent.run(query)
    print(answer)
