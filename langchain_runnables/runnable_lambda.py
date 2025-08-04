from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import (
    RunnableSequence,
    RunnableParallel,
    RunnablePassthrough,
    RunnableLambda,
)

from dotenv import load_dotenv


def word_counter(sentence):
    return len(list(sentence.split()))


load_dotenv()


prompt = PromptTemplate(
    template="write a joke about {topic}", input_variables=["topic"]
)
prompt2 = PromptTemplate(template="Explain the joke {joke}", input_variables=["joke"])
model = ChatOpenAI()
parser = StrOutputParser()

joke_generater_chain = RunnableSequence(prompt, model, parser)
paralled_chain = RunnableParallel(
    {
        "joke": RunnablePassthrough(),
        "lenght of joke": RunnableLambda(word_counter),
        "explanation": RunnableSequence(prompt2, model, parser),
    }
)
final_chain = RunnableSequence(joke_generater_chain, paralled_chain)


print(final_chain.invoke({"topic": "AI"}))
