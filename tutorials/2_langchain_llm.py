from langchain_ollama import ChatOllama

model = ChatOllama(
    model="qwen3:4b-instruct-2507-q4_K_M",
)

response = model.invoke("What is the capital of France?")

print(response.content)
