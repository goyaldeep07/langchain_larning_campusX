from langchain_openai import ChatOpenAI
from langchain_community.tools import tool
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

import requests

load_dotenv()


# tool creation
@tool
def multiply(a: int, b: int) -> int:
    "Multiply tool"
    return a * b


print(multiply.invoke(dict(a=5, b=2)))

# tool binding
model = ChatOpenAI()
llm_with_tools = model.bind_tools(tools=[multiply])

# result = llm_with_tools.invoke('hi how are you')
result = llm_with_tools.invoke("can u multiply 4 and 3")
print(result)

input_dict = result.tool_calls[0]["args"]

r = multiply.invoke(input=input_dict)
print(r)  # 12
r2 = multiply.invoke(result.tool_calls[0])
print(r2)  # content='12' name='multiply' tool_call_id='call_wiH1vzJPCEqPGTHDmthQUjMV'
print(type(r2))  # <class 'langchain_core.messages.tool.ToolMessage'>
