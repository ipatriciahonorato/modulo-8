import os
import openai
from dotenv import load_dotenv
import chainlit as cl
import requests
import time

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Configura a chave de API da OpenAI
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Função para traduzir o texto de português para inglês
async def translate_to_english(text):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Translate the following Portuguese text to English:\n\n{text}",
            max_tokens=60
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Erro ao traduzir: {e}")
        return ""

# Função para obter a resposta em áudio
async def get_audio_response(text):
    response_url = "http://localhost:5000/"
    try:
        audio_response = requests.get(response_url, params={'text': text}).content
        return audio_response
    except Exception as e:
        print(f"Erro ao obter resposta em áudio: {e}")
        return None

# Função principal para responder mensagens
@cl.on_message
async def main(message):
    query = message.content  # Texto em português

    # Traduz para inglês
    english_translation = await translate_to_english(query)

    # Obtém a resposta em áudio
    audio_response = await get_audio_response(english_translation)

    # Envia tanto a resposta em texto quanto em áudio para o usuário
    elements = [cl.Audio(name="response", display="inline", content=audio_response)]
    text_message = cl.Message(elements=elements, content=english_translation)
    await text_message.send()

if __name__ == '__main__':
    cl.run()


