import json

from langchain.tools import tool
from langchain_tavily import TavilySearch

from dotenv import load_dotenv

load_dotenv()


@tool
def multiply_numbers(a: float, b: float) -> float:
    """Multiply two numbers together."""
    result = a * b
    return result


tavily_search = TavilySearch(max_results=5)

multiply_result = multiply_numbers.invoke({"a": 2, "b": 3})
print(multiply_result)
print("\n" * 2 + "-" * 100 + "\n" * 2)

tavily_result = tavily_search.invoke(
    "What was the result of Real Madrid's match this weekend?"
)
print(json.dumps(tavily_result, indent=2))
