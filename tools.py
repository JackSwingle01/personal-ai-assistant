from langchain.agents import Tool
from web_search import web_search
from wiki import get_wiki_summary
from langchain.chains import LLMMathChain
from chain import make_simple_chat_chain
from config import CHAT_MODEL
chat = CHAT_MODEL

llm_chain = make_simple_chat_chain(
    sys_msg_template="Try and respond to the user's message. If you don't know the answer, say 'I don't know'.",
    user_msg_template="{input}",
    input_key="input",
    output_key="output",
    verbose=True
)

llm_tool = Tool(
    name="language_model",
    description="""
    Talk with a large language model. 
    Useful for general knowledge and logic. 
    Also useful for things that aren't questions. 
    Try this if no other tools seem appropriate.
    """,
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