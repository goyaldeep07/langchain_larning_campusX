from langchain_community.tools import tool


@tool
def add(a: int, b: int) -> int:
    """Addition function"""
    return a + b


@tool
def multiply(a: int, b: int) -> int:
    """Multiply function"""
    return a * b


class MathToolkit:
    def get_tools(self):
        return [add, multiply]


if __name__ == "__main__":
    toolkit = MathToolkit()
    list_of_tools = toolkit.get_tools()

    for tool in list_of_tools:
        print(tool.name)
        print(tool.invoke({"a": 5, "b": 6}))
