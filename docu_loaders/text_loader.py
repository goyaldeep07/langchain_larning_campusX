from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI()

prompt = PromptTemplate(
    template="Write a summary for the following poem - \n {poem}",
    input_variables=["poem"],
)
parser = StrOutputParser()
loader = TextLoader("docu_loaders/cricket.txt", encoding="utf-8")

docs = loader.load()

print(type(docs[0]))  # <class 'langchain_core.documents.base.Document'>
print(docs[0].metadata)  # {'source': 'docu_loaders/cricket.txt'}
poem = docs[0].page_content


chain = prompt | model | parser
summary = chain.invoke({"poem": poem})
print(summary)
