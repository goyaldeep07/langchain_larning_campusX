from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import (
    RunnableSequence,
    RunnableParallel,
    RunnablePassthrough,
)

from dotenv import load_dotenv


load_dotenv()


prompt = PromptTemplate(
    template="write a joke about {topic}", input_variables=["topic"]
)
prompt2 = PromptTemplate(template="Explain the joke {joke}", input_variables=["joke"])
model = ChatOpenAI()
parser = StrOutputParser()

chain = RunnableSequence(prompt, model, parser, prompt2, model, parser)
print(chain.invoke({"topic": "AI"}))
