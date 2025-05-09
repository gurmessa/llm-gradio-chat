# Ollama Gradio Chat Interface

A simple chat interface combining Ollama's AI capabilities with Gradio's UI framework.

## Features
- Local AI chat using Ollama
- Gradio web interface
- Markdown rendering support
- Conversation history

## Requirements
- Python 3.8+
- Ollama installed and running locally

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```bash
python ollama_gradio_chat.py
```

The application will start a local server at http://localhost:7860

## Configuration
Edit `ollama_gradio_chat.py` to:
- Change the default model
- Modify UI layout
- Adjust temperature settings

## Dependencies
Listed in requirements.txt:
- gradio
- ollama
- markdown
