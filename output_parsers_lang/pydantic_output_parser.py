from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

model = ChatOpenAI()


class Person(BaseModel):
    name: str = Field(..., description="The name of the person")
    age: int = Field(..., description="The age of the person", gt=18)
    city: str = Field(..., description="The city where the person lives")


parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template="generate the name, age and city of a fictional {place} person \n {format_instructions}",
    input_variables=["place"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)
"""
input_variables=['place'] input_types={} partial_variables={'format_instructions': 'The output should be formatted as a JSON instance that conforms to the JSON schema below.\n\nAs an example, for the schema {"properties": {"foo": {"title": "Foo", "description": "a list of strings", "type": "array", "items": {"type": "string"}}}, "required": ["foo"]}\nthe object {"foo": ["bar", "baz"]} is a well-formatted instance of the schema. The object {"properties": {"foo": ["bar", "baz"]}} is not well-formatted.\n\nHere is the output schema:\n```\n{"properties": {"name": {"description": "The name of the person", "title": "Name", "type": "string"}, "age": {"description": "The age of the person", "exclusiveMinimum": 18, "title": "Age", "type": "integer"}, "city": {"description": "The city where the person lives", "title": "City", "type": "string"}}, "required": ["name", "age", "city"]}\n```'} template='generate the name, age and city of a fictional {place} person \n {format_instructions}'
"""
print(template)
# chain = template | model | parser
# result_chain = chain.invoke({"place": "south african"})
# prompt = template.format(place="Nepalese")
# result = model.invoke(prompt)
# final_result = parser.parse(result.content)

# print(result_chain)
# print(type(result_chain))
