from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel

from dotenv import load_dotenv


load_dotenv()

prompt1 = PromptTemplate(
    template="generate a tweet about {topic}", input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="generate a linkedin post about {topic}", input_variables=["topic"]
)

model = ChatOpenAI()
parser = StrOutputParser()

paralled_chain = RunnableParallel(
    {
        "tweet": RunnableSequence(prompt1, model, parser),
        "linkedin_post": RunnableSequence(prompt2, model, parser),
    }
)

result = paralled_chain.invoke({"topic", "AI"})
print(result)
