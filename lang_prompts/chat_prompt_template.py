from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# this is not working in the current version of langchain
"""messages=[SystemMessage(content='You are a helpful {domain} assistant.', additional_kwargs={}, response_metadata={}), HumanMessage(content='Explain in simple terms: what is {question}', additional_kwargs={}, response_metadata={})]"""
# chat_template = ChatPromptTemplate.from_messages([
#     SystemMessage(content="You are a helpful {domain} assistant."),
#     HumanMessage(content="Explain in simple terms: what is {question}"),
# ])

# # this works
"""messages=[SystemMessage(content='You are a helpful computer science assistant.', additional_kwargs={}, response_metadata={}), HumanMessage(content='Explain in simple terms: what is quantum computing', additional_kwargs={}, response_metadata={})]"""

chat_template = ChatPromptTemplate([
    ('system', "You are a helpful {domain} assistant."),
    ('human', "Explain in simple terms: what is {question}")
])

prompt = chat_template.invoke(input=dict(domain="computer science", question="quantum computing"))
print(prompt)