# AI Chat Interfaces

Four implementations of Gradio chat interfaces with streaming and standard versions for both Ollama (local AI) and OpenRouter (cloud AI).

## Features

**Ollama Implementations:**
- Local AI chat using Ollama
- Markdown rendering
- Conversation history
- `ollama_gradio_chat.py`: Basic implementation
- `ollama_gradio_chat_with_streaming.py`: Real-time streaming support

**OpenRouter Implementations:**
- Cloud-based AI models via OpenRouter
- API key configuration
- Multiple model support
- `openrouter_gradio_chat.py`: Standard implementation
- `openrouter_gradio_chat_streaming.py`: Streaming response support

## Requirements
- Python 3.8+
- Ollama installed and running (for local versions)
- OpenRouter API key (for cloud versions)

## Installation
```bash
pip install -r requirements.txt
cp .env.example .env  # For OpenRouter configuration
```

## Usage

**Ollama Chat:**
```bash
# Standard version
python ollama_gradio_chat.py

# Streaming version
python ollama_gradio_chat_with_streaming.py
```

**OpenRouter Chat:**
```bash
# Standard version
python openrouter_gradio_chat.py

# Streaming version 
python openrouter_gradio_chat_streaming.py
```

All applications start a local server at http://localhost:7860


**OpenRouter Setup:**
1. Create API key: [OpenRouter Keys](https://openrouter.ai/settings/keys)
2. Choose a model: [OpenRouter Models](https://openrouter.ai/models)

**Ollama Setup:**
Ollama Installation[Installation](https://github.com/ollama/ollama)


## Configuration
1. OpenRouter: Set `OPENROUTER_API_KEY` in `.env`
2. Ollama: Edit respective files to:
   - Change default model (default: llama3.2)
   - Adjust temperature
   - Modify UI layout
3. OpenRouter: Edit respective files to:
   - Select different models
   - Adjust response length
   - Modify system prompts

## Dependencies
- gradio
- ollama
- markdown
- python-dotenv (for OpenRouter versions)