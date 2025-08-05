from langchain_openai.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.schema import Document
from dotenv import load_dotenv


load_dotenv()
doc1 = Document(
    page_content="""Virat Kohli is the highest run-scorer in IPL history, having played his entire career with Royal Challengers Bangalore.
He led RCB for several seasons but is yet to win an IPL title despite consistent individual performances.""",
    metadata={"team": "Royal challengers bangluru"},
)

doc2 = Document(
    page_content="""Rohit Sharma is one of the most successful IPL captains, leading Mumbai Indians to five titles.
He is known for his calm leadership and match-winning knocks at the top of the order.""",
    metadata={"team": "Mumbai Indians"},
)

doc3 = Document(
    page_content="""Bumrah emerged as a world-class death-over specialist while playing for Mumbai Indians.
His toe-crushing yorkers and consistency have been crucial to MI's bowling success.""",
    metadata={"team": "Mumbai Indians"},
)

doc4 = Document(
    page_content="""MS Dhoni is the iconic leader of Chennai Super Kings, under whom CSK has won five IPL titles.
His finishing ability and cool captaincy have made him a legend in IPL history.""",
    metadata={"team": "Chennai Super Kings"},
)

doc5 = Document(
    page_content="""Jadeja has been a vital all-rounder for CSK, contributing with both bat and ball across many seasons.
He captained CSK briefly and played a key role in their 2023 title-winning campaign.""",
    metadata={"team": "Chennai Super Kings"},
)

docs = [doc1, doc2, doc3, doc4, doc5]

vector_store = Chroma(
    embedding_function=OpenAIEmbeddings(),
    persist_directory="chroma_db",
    collection_name="sample",
)

# create
# vector_store.add_documents(documents=docs)

# read
d = vector_store.get(include=["embeddings", "documents", "metadatas"])
print(d)

# retrieve
result = vector_store.similarity_search(query="bowler", k=2)
# print(result)

result2 = vector_store.similarity_search_with_score(
    query="bowler", k=2
)  # low means near to our query
# print(result2)

result3 = vector_store.similarity_search_with_score(
    query="", filter={"team": "Chennai Super Kings"}
)
# print(result3)

# update
updated_doc1 = Document(
    page_content="virat kohli, the former captain of Royal Challengers Bangalore (RCB), is renowned for his aggressive leadership and consistency.",
    metadata={"team": "Royal Challengers Bangalore"},
)
# vector_store.update_document(document_id='d23e22bd-2cc4-44fe-b323-5eb881a00356', document=updated_doc1)

# delete
# vector_store.delete(ids=['d271a948-946b-46a4-b6f8-5ddca1327d1a'])
