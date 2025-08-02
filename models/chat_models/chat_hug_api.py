from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()
# print(os.getenv("HUGGINGFACEHUB_API_TOKEN"))
# llm = HuggingFaceEndpoint(
#     repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
# )
llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0"
)
print(f'llm:{llm}')

model = ChatHuggingFace(llm=llm)
print(f'model:{model}')
response = model.invoke("What is the capital of India?")  # Example usage
print(response.content)  # Output the response from the model