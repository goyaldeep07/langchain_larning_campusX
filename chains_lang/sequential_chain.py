from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

model = ChatOpenAI()


prompt1 = PromptTemplate(
    template="Write a detailed report on the following topic: {topic} within 200 words",
    input_variables=["topic"],
)

prompt2 = PromptTemplate(
    template="Write a 5 line summary on the following topic: {topic}",
    input_variables=["topic"],
)

parser = StrOutputParser()
chain = prompt1 | model | parser | prompt2 | model | parser
result_chain = chain.invoke(
    {"topic": "Climate Change and its Impact on Global Weather Patterns"}
)
print(result_chain)
