from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

response = model.invoke("What is the capital of India?")  # Example usage

print(response.content)  # Output the response from the model