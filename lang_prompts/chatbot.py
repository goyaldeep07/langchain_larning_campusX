from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv


load_dotenv()

model = ChatOpenAI()

chat_history = [SystemMessage(content="You are a helpful assistant.")]
while True:
    input_text = input("You: ")
    chat_history.append(HumanMessage(content=input_text))
    if input_text.lower() == "exit":
        break
    response = model.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))
    print("AI:", response.content)  # Output the response from the model
print("Chat history:", chat_history)  # Print the entire chat history
