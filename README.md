# AI Chat Interfaces

Dual implementation of chat interfaces using both Ollama (local AI) and OpenRouter (cloud AI) with Gradio UI.

## Features

**Ollama Version:**
- Local AI chat using Ollama
- Streaming response support
- Markdown rendering
- Conversation history

**OpenRouter Version:**
- Cloud-based AI models via OpenRouter
- API key configuration
- Multiple model support
- Response customization

## Requirements
- Python 3.8+
- Ollama installed and running (for local version)
- OpenRouter API key (for cloud version)

## Installation
```bash
pip install -r requirements.txt
cp .env.example .env  # For OpenRouter configuration
```

## Usage

**Ollama Chat:**
```bash
python ollama_gradio_chat_with_streaming.py
```

**OpenRouter Chat:**
```bash
python openrouter_gradio_chat.py
```

Both applications start a local server at http://localhost:7860

## Configuration
1. OpenRouter: Set `OPENROUTER_API_KEY` in `.env`
2. Ollama: Edit `ollama_gradio_chat_with_streaming.py` to:
   - Change default model (default: llama2)
   - Adjust temperature
   - Modify UI layout
3. OpenRouter: Edit `openrouter_gradio_chat.py` to:
   - Select different models
   - Adjust response length
   - Modify system prompts

## Dependencies
- gradio
- ollama
- markdown
- python-dotenv (for OpenRouter version)
