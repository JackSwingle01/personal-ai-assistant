from langchain.prompts.chat import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate
from langchain.chains import LLMChain

from config import CHAT_MODEL


def make_simple_chat_templates(sys_msg_template: str, user_msg_template: str, input_key: str) -> list:
    templates = []
    templates.append(SystemMessagePromptTemplate.from_template(
        input_variables=[],
        template=sys_msg_template
    ))
    templates.append(HumanMessagePromptTemplate.from_template(
        input_variables=[input_key],
        template=user_msg_template
    ))
    return templates


def get_chat_chain(templates: list, output_key: str, chat_model=CHAT_MODEL, verbose: bool = False) -> LLMChain:
    # combined template:
    template = ChatPromptTemplate.from_messages(templates)
    # create link:
    link = LLMChain(
        llm=chat_model,
        prompt=template,
        output_key=output_key,
        verbose=verbose)

    return link


def make_simple_chat_chain(
        sys_msg_template: str,
        user_msg_template: str,
        input_key: str,
        output_key: str = "output",
        verbose: bool = False
) -> LLMChain:
    templates = make_simple_chat_templates(
        sys_msg_template,
        user_msg_template,
        input_key
    )
    chain = get_chat_chain(templates=templates,
                           output_key=output_key,
                           verbose=verbose)
    return chain
