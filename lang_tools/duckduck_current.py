from langchain_community.tools import Tool
from datetime import datetime, date
import requests


today = date.today().isoformat()


def search_ddgs(query: str) -> str:
    full_query = f"{query} - {today}"
    url = f"https://duckduckgo.com/html?q={full_query}"
    return f"Search URL: {url}"


ddgs_tool = Tool(
    name="DuckDuckGoSearch",
    func=search_ddgs,
    description="Useful for searching current topics on the web using DuckDuckGo with today's date.",
)

response = ddgs_tool.invoke("SSC CGL update")
print(response)
