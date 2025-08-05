from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI()

prompt = PromptTemplate(
    template="Answer the following questions - \n {question} from the following text - \n {text}",
    input_variables=["question", "text"],
)

parser = StrOutputParser()

url = "https://www.amazon.in/V50-Storage-Additional-Exchange-Offers/dp/B0DTHVHZC5/ref=sr_1_3?adgrpid=55710945821&dib=eyJ2IjoiMSJ9.sQDvwgXOTwGt18eeJl3OaYf7r1q1Fip_DbR3S4UbKyzwcRlTBM9x0F-veOOOCYP0oAO9-VVe2Ix_W6Wt57IdE6fAdKcpYlJcFS_iKHvyXqBYmUYMXL5aGPgv7VQNL7nEiikPhjG-qhSBQf1KCu76dRO97ZAV47DmfM3JLd20i2ZEk0TF4efmJrztFPxXhq2-57fdFPoVF4gG8QvPKlETItShkq3SGLYyUBgES5s64fk.tEH6dl3WiH-KN2zfCaaDJCcpJsuobIYJ_FyN18PyyjE&dib_tag=se&ext_vrnc=hi&hvadid=590653753114&hvdev=c&hvlocphy=9184819&hvnetw=g&hvqmt=e&hvrand=17967856677877084825&hvtargid=kwd-697444400527&hydadcr=27739_2266894&keywords=vivo%2Bv50&mcid=23ae89f79fc630d382851d67718bf18f&nsdOptOutParam=true&qid=1754374504&sr=8-3&th=1"

loader = WebBaseLoader(web_path=url)
docs = loader.load()

content = docs[0].page_content

chain = prompt | model | parser
result = chain.invoke(
    {"question": "what is the product that we are talking about", "text": content}
)

print(result)
