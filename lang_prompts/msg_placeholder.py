from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


chat_template = ChatPromptTemplate(
    [
        ("system", "You are a helpful {domain} assistant."),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "Explain in simple terms: what is {question}"),
    ]
)

chat_history = []

with open("lang_prompts/chat_history.txt", "r") as file:
    for line in file:
        chat_history.append(line.strip())

prompt = chat_template.invoke(
    {
        "domain": "computer science",
        "question": "quantum computing",
        "chat_history": chat_history,
    }
)
print(prompt)
