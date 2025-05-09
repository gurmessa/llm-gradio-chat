import gradio as gr
import ollama

OLLAMA_MODEL = "llama3.2:latest" 

def chat_with_ollama(message, history):
    messages = []

    # Add previous conversation history
    for human, assistant in history:
        messages.append({"role": "user", "content": human})
        messages.append({"role": "assistant", "content": assistant})

    # Add the current user message
    messages.append({"role": "user", "content": message})

    try:
        response = ollama.chat(model=OLLAMA_MODEL, messages=messages, stream=True)
        
        # Stream the response
        full_response = ""
        for chunk in response:
            if 'message' in chunk and 'content' in chunk['message']:
                content = chunk['message']['content']
                full_response += content
                yield full_response # Yield the accumulating response for streaming
                
    except Exception as e:
        return f"Error: {e}"


# Create the Gradio ChatInterface
demo = gr.ChatInterface(
    fn=chat_with_ollama,
    title=f"Chat with {OLLAMA_MODEL} powered by Ollama"
)

# Launch the Gradio app
if __name__ == "__main__":
    demo.launch()