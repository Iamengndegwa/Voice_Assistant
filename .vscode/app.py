import gradio as gr
from huggingface_hub import InferenceClient

client = InferenceClient("mistralai/Mistral-7B-Instruct-v0.3")

def chat(user_message, history):
    if not user_message.strip():
        return "", history
    
    messages = [{"role": "system", "content": "You are a helpful, friendly assistant."}]
    
    for human, assistant in history:
        messages.append({"role": "user", "content": human})
        messages.append({"role": "assistant", "content": assistant})
    
    messages.append({"role": "user", "content": user_message})
    
    try:
        response = client.chat_completion(messages=messages, max_tokens=500)
        reply = response.choices[0].message.content
    except Exception as e:
        reply = f"Error: {str(e)}"
    
    history.append((user_message, reply))
    return "", history

with gr.Blocks(title="AI Voice Assistant") as demo:
    gr.Markdown("# 🎙️ AI Voice Assistant")
    gr.Markdown("Powered by **Mistral-7B** via Hugging Face — completely free!")
    
    chatbot = gr.Chatbot(height=450)
    
    with gr.Row():
        msg = gr.Textbox(placeholder="Type your message and press Enter...", scale=4, container=False)
        send_btn = gr.Button("Send 🚀", scale=1, variant="primary")
    
    clear_btn = gr.Button("🗑️ Clear Conversation", variant="secondary")
    
    msg.submit(chat, [msg, chatbot], [msg, chatbot])
    send_btn.click(chat, [msg, chatbot], [msg, chatbot])
    clear_btn.click(lambda: ([], ""), None, [chatbot, msg])

if __name__ == "__main__":
    demo.launch()