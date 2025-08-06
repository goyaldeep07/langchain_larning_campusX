from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.tools import ddg_search

search_tool = ddg_search.DuckDuckGoSearchRun()

results = search_tool.invoke("ind vs england test series")
print(results)
