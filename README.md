# Local AI Agent
https://www.youtube.com/watch?v=8HP_yVz7Gg8


A simple starting point for building AI agents with Python, showcasing some really cool libraries and technologies:

- **LangChain/LangGraph** - Build powerful AI workflows and agents
- **Ollama** - Run AI models locally on your machine
- **Chainlit** - Beautiful chat UI for your AI agents

## Prerequisites

Make sure you have these installed:

1. **uv** - Fast Python package manager ([installation guide](https://docs.astral.sh/uv/getting-started/installation/))
   ```bash
   # macOS
   brew install uv
   ```

2. **Ollama** - Local AI model runtime ([download page](https://ollama.com/download/mac))
   ```bash
   # macOS
   brew install ollama
   ```

3. Pull the AI model used in this project:
   ```bash
   ollama pull qwen3:4b-instruct-2507-q4_K_M
   ```

## Running the Agent

This is a single-file script with inline dependencies. Just run:

```bash
uv run main.py
```

That's it! The UI will be ready in your browser at `http://localhost:8000`

## What It Does

The example agent is a friendly math assistant named Samantha that can:
- Add numbers together
- Multiply numbers
- Chat with you conversationally

Try asking: "What's 42 plus 17?"

## Build Your Own

This is meant as a starting point. Fork it, modify the tools, change the system prompt, structure better the code and build something amazing!
