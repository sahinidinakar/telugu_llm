import gradio as gr
import random
import time


with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])


    def respond(message, chat_history):
        bot_message = answer_query(message)
        chat_history.append((message, bot_message))
        time.sleep(2)
        return "", chat_history


    msg.submit(respond, [msg, chatbot], [msg, chatbot])


demo.launch(share=True)