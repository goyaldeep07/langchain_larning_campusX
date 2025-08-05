from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader


dir_load = DirectoryLoader(
    path="docu_loaders/books", glob="*.pdf", loader_cls=PyPDFLoader
)

# docs = dir_load.load()
docs = dir_load.lazy_load()

for doc in docs:
    print(doc.metadata)
# print(len(docs))
