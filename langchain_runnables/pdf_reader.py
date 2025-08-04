from langchain_openai import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import openai
from langchain.vectorstores import FAISS
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from dotenv import load_dotenv

load_dotenv()

# Load the document
loader = TextLoader("docs.txt")  # Ensure docs.txt exists
documents = loader.load()


# Split the text into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = text_splitter.split_documents(documents=documents)


# convert text into embeddings & store in FAISS
vector_store = FAISS.from_documents(docs, OpenAIEmbeddings())

# create a retriever (fetches relevant documents)
retriever = vector_store.as_retriever()

# Manually retrieve relevant documents
query = "What are the key take aways from the document?"
retrieved_docs = retriever.get_relevant_documents(query)

# combine retrieved text into a single prompt
retrieved_text = "\n".join([doc.page_content for doc in retrieved_docs])

# Initialize the llm
llm = ChatOpenAI()


# Manually Pass Retrieved Text to LLM
prompt = (
    f"Based on the following text, answer the following: {query}\n\n{retrieved_text}"
)
answer = llm.predict(prompt)


print(f"Answer: {answer}")
