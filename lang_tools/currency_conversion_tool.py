from langchain_openai import ChatOpenAI
from langchain_community.tools import tool
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import os
import json
import requests
from langchain_core.tools import InjectedToolArg
from typing import Annotated


load_dotenv()
EXCHANGE_RATE_API_KEY = os.getenv("EXCHANGE_RATE_API_KEY")


@tool
def get_conversion_factor(base_currency: str, target_currency: str) -> float:
    """This function fetches the currency conversion factor between a given base currency and a target currency"""
    """GET https://v6.exchangerate-api.com/v6/YOUR-API-KEY/pair/EUR/GBP"""
    url = f"https://v6.exchangerate-api.com/v6/{EXCHANGE_RATE_API_KEY}/pair/{base_currency}/{target_currency}"
    response = requests.get(url=url)
    try:
        return response.json()["conversion_rate"]
    except Exception as e:
        return None


@tool
def convert(
    base_currency_value: int, conversion_rate: Annotated[float, InjectedToolArg]
) -> float:
    """given a currency conversion rate this function calculates the target currency value from a given base currency value"""
    return base_currency_value * conversion_rate


conversion_rate = get_conversion_factor.invoke(
    {"base_currency": "USD", "target_currency": "INR"}
)
result = convert.invoke(dict(base_currency_value=10, conversion_rate=conversion_rate))
print(result)

model = ChatOpenAI()
model_with_tool = model.bind_tools([get_conversion_factor, convert])

messages = [
    HumanMessage(
        "what is the conversion factor between usd and inr, and based on that can you convert 10 usd into inr"
    )
]
ai_msg = model_with_tool.invoke(messages)
messages.append(ai_msg)
tool_calls = ai_msg.tool_calls
# with out InjectedToolArg
# [{'name': 'get_conversion_factor', 'args': {'base_currency': 'USD', 'target_currency': 'INR'}, 'id': 'call_9ddI3x7NOAUuvk69JfUxTAil', 'type': 'tool_call'}, {'name': 'convert', 'args': {'base_currency_value': 10, 'conversion_rate': 73.69}, 'id': 'call_Qk1jGSFURjaF10hx0o8EV7WM', 'type': 'tool_call'}]

# with InjectedToolArg
# [{'name': 'get_conversion_factor', 'args': {'base_currency': 'USD', 'target_currency': 'INR'}, 'id': 'call_dTGwtYbdVZXwrlm7r1v4BIFi', 'type': 'tool_call'}, {'name': 'convert', 'args': {'base_currency_value': 10}, 'id': 'call_2XsDvrmqHtCgRip9tswgerFS', 'type': 'tool_call'}]

for tool_call in tool_calls:
    print(type(tool_call))
    if tool_call["name"] == "get_conversion_factor":
        tool_msg1 = get_conversion_factor(tool_call["args"])
        messages.append(tool_msg1)
        conversion_rate = tool_msg1
    elif tool_call["name"] == "convert":
        tool_call["args"]["conversion_rate"] = conversion_rate
        tool_msg2 = convert(tool_call["args"])
        messages.append(tool_msg2)

print(messages)
