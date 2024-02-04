# Crea y configura el LLMChain
from langchain_openai import OpenAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory, ConversationBufferWindowMemory
from model.config import OPENAI_API_KEY, OPENAI_BASE_URL

def create_llm_chain(role):
    llm = OpenAI(openai_api_key=OPENAI_API_KEY, base_url=OPENAI_BASE_URL, temperature = 0.9, max_tokens = 2000, top_p = 0.9, frequency_penalty = 0.5, presence_penalty = 0.5)
    prompt = ChatPromptTemplate(messages=[SystemMessagePromptTemplate.from_template(role[1]), MessagesPlaceholder(variable_name="chat_history"), HumanMessagePromptTemplate.from_template("{question}")])
    print(prompt)
    memory = ConversationBufferWindowMemory(memory_key="chat_history", return_messages=True, k=6)
    return LLMChain(llm=llm, verbose=False, memory=memory,prompt=prompt, output_parser=StrOutputParser())
