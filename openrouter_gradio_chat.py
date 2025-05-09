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
    messages = history

    # Add the current user message
    messages.append({"role": "user", "content": message})

    try:
        completion =client.chat.completions.create(
            model=OPENROUTER_MODEL, 
            messages=messages, 
        )

        return completion.choices[0].message.content

    except Exception as e:
        return f"Error: {e}"


# Create the Gradio ChatInterface
demo = gr.ChatInterface(
    fn=chat_with_openrouter,
    title=f"Chat with {OPENROUTER_MODEL} powered by OpenRouter",
    type="messages" 
)

# Launch the Gradio app
if __name__ == "__main__":
    demo.launch()
