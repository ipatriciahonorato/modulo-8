from flask import Flask, request, Response
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize Flask application
app = Flask(__name__)

# Initialize OpenAI client with API key from .env file
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

@app.route("/")
def hello_world():
    # Get the input text from query parameter
    input_text = request.args.get('text', '')

    # Generate speech using OpenAI's API
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=input_text
    )

    # Fetch audio data using the content property
    audio_data = response.content

    # Return audio data as a response
    return Response(audio_data, mimetype="audio/mpeg")

if __name__ == "__main__":
    app.run(debug=True)
