from langchain_openai import ChatOpenAI, OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model="gpt-3.5-turbo-instruct")

response = llm.invoke("What is the capital of India?")  # Example usage
print(response)  # Output the response from the model
