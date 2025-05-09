from dotenv import load_dotenv
from openai import OpenAI
import gradio as gr
import os

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
)

OPENROUTER_MODEL = "qwen/qwen3-32b:free"

def chat_with_openrouter(message, history):
    messages = []

    # Add the current user message
    messages.append({"role": "user", "content": message})

    try:
        # Create a streaming chat completion
        stream = client.chat.completions.create(
            model=OPENROUTER_MODEL,
            messages=messages,
            stream=True  # Enable streaming
        )

        # Initialize response
        full_response = ""

        # Stream the response chunks
        for chunk in stream:
            if chunk.choices and chunk.choices[0].delta and chunk.choices[0].delta.content:
                content = chunk.choices[0].delta.content
                full_response += content
                yield full_response  # Yield partial response for real-time display

    except Exception as e:
        yield f"Error: {e}"

# Create the Gradio ChatInterface
demo = gr.ChatInterface(
    fn=chat_with_openrouter,
    title=f"Chat with {OPENROUTER_MODEL} powered by OpenRouter",
    examples=["Tell me a short story", "What is the capital of France?"],
    theme=gr.themes.Soft(),
    type="messages"
)


# Launch the Gradio app
if __name__ == "__main__":
    demo.launch() 