from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal, Annotated


class Feedback(BaseModel):
    sentiment: Annotated[
        Literal["Positive", "Negative"],
        Field(description="Give the sentiment of the feedback"),
    ]


load_dotenv()

model = ChatOpenAI()

parser1 = StrOutputParser()
parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template="Classify the sentiment of the following feedback text into positive or negative \n {feedback} \n {format_instruction}",
    input_variables=["feedback"],
    partial_variables={"format_instruction": parser2.get_format_instructions()},
)

prompt_positive = PromptTemplate(
    template="Write an appropriate response to this positive feedback \n {feedback}",
    input_variables=["feedback"],
)

prompt_negative = PromptTemplate(
    template="Write an appropriate response to this negative feedback \n {feedback}",
    input_variables=["feedback"],
)
classifier_chain = prompt1 | model | parser2

branch_chain = RunnableBranch(
    (lambda x: x.sentiment == "Positive", prompt_positive | model | parser1),
    (lambda x: x.sentiment == "Negative", prompt_negative | model | parser1),
    RunnableLambda(lambda x: "could not find sentiment"),
)

chain = classifier_chain | branch_chain
chain.invoke({"feedback": "This is a terrible phone."})

chain.get_graph().print_ascii()
