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


# print(multiply.invoke(dict(a=5, b=2)))

# tool binding
model = ChatOpenAI()
llm_with_tools = model.bind_tools(tools=[multiply])

messages = []
messages.append(HumanMessage("can u multiply 4 and 3"))
# result = llm_with_tools.invoke('hi how are you')
result = llm_with_tools.invoke(messages)
messages.append(result)


r2 = multiply.invoke(result.tool_calls[0])
messages.append(r2)
print(r2)  # content='12' name='multiply' tool_call_id='call_wiH1vzJPCEqPGTHDmthQUjMV'
print(type(r2))  # <class 'langchain_core.messages.tool.ToolMessage'>

print()
print(messages)
"""
[
HumanMessage(content='can u multiply 4 and 3', additional_kwargs={}, response_metadata={}), 
AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_uBFU0IO0sgSxCfrH07FdXQrM', 'function': {'arguments': '{"a":4,"b":3}', 'name': 'multiply'}, 'type': 'function'}], 'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 17, 'prompt_tokens': 52, 'total_tokens': 69, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-3.5-turbo-0125', 'system_fingerprint': None, 'id': 'chatcmpl-C1Yzuf6SqitBlXC7yWvu6tjCQw3HM', 'service_tier': 'default', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run--c5625b8a-669d-4ec6-9ad8-b2ec4c497daa-0', tool_calls=[{'name': 'multiply', 'args': {'a': 4, 'b': 3}, 'id': 'call_uBFU0IO0sgSxCfrH07FdXQrM', 'type': 'tool_call'}], usage_metadata={'input_tokens': 52, 'output_tokens': 17, 'total_tokens': 69, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}), 
ToolMessage(content='12', name='multiply', tool_call_id='call_uBFU0IO0sgSxCfrH07FdXQrM')]
"""


print(llm_with_tools.invoke(messages).content)
