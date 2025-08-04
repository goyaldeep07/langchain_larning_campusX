from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


model = ChatOpenAI()
# model = HuggingFaceEndpoint(
# repo_id="google/gemma-2-2b-it",
# task="text-generation"
# )

template1 = PromptTemplate(
    template="Write a detailed report on the following topic: {topic} within 200 words",
    inputs_variables=["topic"],
)
template2 = PromptTemplate(
    template="Write a 5 line summary on the following topic: {topic}",
    input_variables=["topic"],
)

# this is the way without using parser and chaining
# prompt1 = template1.format(topic="Artificial Intelligence in Healthcare")
# result = model.invoke(prompt1)
#
# prompt2 = template2.format(topic=result.content)
# result2 = model.invoke(prompt2)
# print(result2.content)


# this is the way with parser and chaining
parser = StrOutputParser()
chain = template1 | model | parser | template2 | model | parser
result_chain = chain.invoke(
    {"topic": "Climate Change and its Impact on Global Weather Patterns"}
)
print(result_chain)
