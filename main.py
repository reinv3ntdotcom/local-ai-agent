# /// script
# dependencies = [
#   "chainlit==2.6.0",
#   "langchain==1.0.2",
#   "langchain-ollama==1.0.0",
#   "langgraph==1.0.1",
#   "loguru==0.7.3",
#   "langchain-tavily==0.2.12"
# ]
# ///


import chainlit as cl
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from langgraph.checkpoint.memory import InMemorySaver
from loguru import logger
from langchain_tavily import TavilySearch

model = ChatOllama(
    model="qwen3:4b-instruct-2507-q4_K_M",
)


@tool
def sum_numbers(a: float, b: float) -> float:
    """Sum two numbers together."""
    result = a + b
    logger.info(f"➕ Calculating sum: {a} + {b} = {result}")
    return result


@tool
def multiply_numbers(a: float, b: float) -> float:
    """Multiply two numbers together."""
    result = a * b
    logger.info(f"✖️ Calculating product: {a} × {b} = {result}")
    return result


tavily_search = TavilySearch(max_results=5)

tools = [sum_numbers, multiply_numbers, tavily_search]

system_prompt = """You are Samantha, a helpful assistant with a warm personality.
You can help with basic math operations and web searches by using your tools.
Always use the tools when asked to do math calculations or search for information online.
Keep your responses friendly and conversational."""

checkpointer = InMemorySaver()

math_agent = create_agent(
    model=model,
    tools=tools,
    system_prompt=system_prompt,
    checkpointer=checkpointer,
)


@cl.on_message
async def on_message(msg: cl.Message):
    final_answer = cl.Message(content="")

    for message_chunk, metadata in math_agent.stream(
        {"messages": [HumanMessage(content=msg.content)]},
        {"configurable": {"thread_id": "1"}},
        stream_mode="messages",
    ):
        if message_chunk.content and metadata["langgraph_node"] == "model":
            await final_answer.stream_token(message_chunk.content)

    await final_answer.send()


if __name__ == "__main__":
    from chainlit.cli import run_chainlit

    run_chainlit(__file__)
