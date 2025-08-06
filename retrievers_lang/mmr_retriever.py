from langchain.schema import Document
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv


load_dotenv()


# Sample documents
docs = [
    Document(page_content="LangChain makes it easy to work with LLMs."),
    Document(page_content="LangChain is used to build LLM based applications."),
    Document(page_content="Chroma is used to store and search document embeddings."),
    Document(page_content="Embeddings are vector representations of text."),
    Document(
        page_content="MMR helps you get diverse results when doing similarity search."
    ),
    Document(page_content="LangChain supports Chroma, FAISS, Pinecone, and more."),
]

vector_store = FAISS.from_documents(embedding=OpenAIEmbeddings(), documents=docs)

retriever = vector_store.as_retriever(
    search_type="mmr", search_kwargs={"k": 3, "lambda_mult": 0.5}
)

query = "what is langchain?"
results = retriever.invoke(query)

for i, doc in enumerate(results):
    print(i + 1, doc.page_content)
