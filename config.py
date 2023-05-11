from langchain.chat_models import ChatOpenAI

from SECRET_API_KEY import KEY
OPENAI_API_KEY = KEY
VECTORSTORE_DIRECTORY = "./data/vectorstore"

CHAT_MODEL = ChatOpenAI(openai_api_key=OPENAI_API_KEY, temperature=.25)
