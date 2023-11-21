import os
import gradio as gr
from dotenv import load_dotenv
from langchain.llms import OpenAI

# API Key ChatGPT
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

# Configuração do modelo LLM com streaming
llm = OpenAI(api_key=api_key, model="gpt-3.5-turbo-instruct", max_tokens=512)

def preparar_prompt(pergunta):
    return f"""
    Pergunta do usuário: '{pergunta}'
    Contexto: Normas de segurança em ambientes industriais. Responda primeiro com uma breve explicação, seguida de bullet points que destaquem os principais aspectos ou recomendações relacionadas à pergunta. As respostas devem ser informativas e refletir as melhores práticas e regulamentações do setor industrial.
    """

def chatbot(pergunta):
    resposta = ""
    for chunk in llm.stream(preparar_prompt(pergunta)):
        resposta += chunk
    return resposta


# Define a Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("🤖 Chatbot de Normas de Segurança Industrial")
    prompt = gr.Textbox(label="Faça sua pergunta", placeholder="Exemplo: Quais são os EPIs necessários para operar um torno mecânico?")
    output = gr.Textbox(label="Resposta")
    prompt.change(chatbot, inputs=prompt, outputs=output)

# Inicia a interface
demo.launch()

