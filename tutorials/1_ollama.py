import ollama

response = ollama.chat(
    model="qwen3:4b-instruct-2507-q4_K_M",
    messages=[{"role": "user", "content": "What is the capital of France?"}],
)

print(response["message"]["content"])
