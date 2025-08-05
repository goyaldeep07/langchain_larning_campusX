from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(file_path="splitters/dl-curriculum.pdf")
splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=20, separator="")

# result = splitter.split_text(text=text)
result = splitter.split_documents(loader.load())
print(result[:5])
