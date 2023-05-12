from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent
from langchain.experimental.plan_and_execute import PlanAndExecute, load_agent_executor, load_chat_planner
from tools import web_search_tool, wiki_tool, math_tool, chat_tool, clock_tool, timer_tool

from config import OPENAI_API_KEY
chat = ChatOpenAI(openai_api_key=OPENAI_API_KEY)

tools = [web_search_tool, wiki_tool, math_tool,
         chat_tool, clock_tool, timer_tool]

# planner = load_chat_planner(chat)
# executor = load_agent_executor(chat, tools, verbose=True)
# agent = PlanAndExecute(planner = planner, executer=executor, verbose=True)
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
