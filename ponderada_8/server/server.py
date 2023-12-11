from flask import Flask, request, Response
from openai import OpenAI
from dotenv import load_dotenv
import os

# Carrega as variáveis do ambiente
load_dotenv()

# Inicializa a aplicação
app = Flask(__name__)

# Inicializa OpenAI client com a API key do .env file
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

@app.route("/")
def translate_and_speak():
    input_text = request.args.get('text', '')

    try:
        # Gera a fala usando a API da OpenAI
        response = client.audio.speech.create(
            model="tts-1",
            voice="alloy",
            input=input_text
        )

        # Busca dados de áudio usando a "propriedade content"
        audio_data = response.content

        # Retorna o audio como resposta
        return Response(audio_data, mimetype="audio/mpeg")
    except Exception as e:
        print(f"Erro ao gerar áudio: {e}")
        return Response("Erro ao gerar áudio", status=500)

if __name__ == "__main__":
    app.run(debug=True)

