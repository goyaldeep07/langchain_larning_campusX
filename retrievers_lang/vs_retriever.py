"""Vector store retriever is a part of retriever type based on data source"""

from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from dotenv import load_dotenv


load_dotenv()


documents = [
    Document(page_content="Langchain helps developers build LLM applications easily."),
    Document(
        page_content="chroma is a vector database optimized for LLM-based search."
    ),
    Document(page_content="Embeddings convert text into high-dimensional vectors."),
    Document(page_content="OpenAI provides powerful embedding models."),
]

embed_model = OpenAIEmbeddings()

vs = Chroma.from_documents(
    documents=documents, embedding=embed_model, collection_name="vector_store_retriever"
)


retriever = vs.as_retriever(search_kwargs={"k": 2})

query = "what is chroma used for?"
result = retriever.invoke(query)
for doc in result:
    print(doc)
