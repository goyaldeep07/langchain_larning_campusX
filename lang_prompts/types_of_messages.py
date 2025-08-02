from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv


load_dotenv()

model = ChatOpenAI()

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="What is the capital of India?")
    ]

model_response = model.invoke(messages)
messages.append(AIMessage(model_response.content))
# print(model_response.content)  # Output the response from the model
print(messages)