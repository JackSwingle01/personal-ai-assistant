from langchain.agents import Tool
from web_search import web_search
from wiki import get_wiki_summary
from langchain.chains import LLMMathChain
from chain import make_simple_chat_chain
from clock import get_date_or_time, set_timer
from config import CHAT_MODEL
chat = CHAT_MODEL

llm_chain = make_simple_chat_chain(
    sys_msg_template="Respond to the user's message. If you don't know the answer, say 'I don't know'.",
    user_msg_template="{input}",
    input_key="input",
    output_key="output",
    verbose=True
)

chat_tool = Tool(
    name="chat_reply",
    description="""Useful for conversation, general knowledge, and logic. Try this if no other tools seem appropriate.""",
    func=llm_chain.run
)

web_search_tool = Tool(
    name="web_search",
    description="Search the web for an answer to your question. Useful for niche questions or recent events.",
    func=web_search
)

wiki_tool = Tool(
    name="wikipedia",
    description="Search wikipedia for information about a subject. Useful for information about a well known subject.",
    func=get_wiki_summary
)

math_tool = Tool(
    name="calculator",
    description="Solve a math problem. Useful for solving math problems.",
    func=LLMMathChain.from_llm(chat).run
)

clock_tool = Tool.from_function(
    name="clock",
    description="Get the current time or date. Useful for getting the current time or date. Input by asking for the time or date or both.",
    func=get_date_or_time
)

timer_tool = Tool.from_function(
    name="timer",
    description="Set a timer that counts down seconds. Action Input has to be in seconds. NOTE: Async function, DO NOT wait for the timer to finish.",
    func=set_timer
)