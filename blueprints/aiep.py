from flask import Blueprint, request
from ai import aifuncties as aif
ai_bp = Blueprint('ai', __name__)

from flask import jsonify, send_file
import os
from openai import OpenAI
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
load_dotenv()


client = OpenAI(api_key=os.environ.get('ONZEENVKEY'))


UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@ai_bp.route("/aitest")
def lvs_allestudenten():
  return "aitest v2"

@ai_bp.route("/voice", methods=['POST'])
def voice():
  return aif.voice()

@ai_bp.route("/handle-recording", methods=['POST'])
def handle_recording():
  return aif.handle_recording()
  
@ai_bp.route("/brengrecordover/<recid>", methods=['GET'])
def recording_ai_transcript(recid):
  return aif.recording_ai_transcript(recid)

@ai_bp.route("/allerecs", methods=['GET'])
def allerecs():
  return aif.allerecs()

@ai_bp.route("/praxisvraag/<term>", methods=['GET'])
def praxisvraag(term):
  return aif.praxisvraag(term)

@ai_bp.route('/upload_audio', methods=['POST'])
def upload_audio():
    if 'audio' not in request.files:
        return jsonify({'error': 'Geen audiobestand ontvangen'}), 400

    audio = request.files['audio']
    if audio.filename == '':
        return jsonify({'error': 'Geen bestand geselecteerd'}), 400

    # Sla het audiobestand op
    filename = secure_filename(audio.filename)
    audio_path = os.path.join(UPLOAD_FOLDER, filename)
    audio.save(audio_path)

    # Gebruik OpenAI Whisper voor transcriptie
    transcript = transcribe_audio(audio_path)

    # Verwerk de vertaling
    target_language = request.form.get('target_language', 'en')  # Standaard naar Engels
    translated_text = translate_text(transcript, target_language)

    audio_filename = text_to_speech_openai(translated_text)

    # Return de transcriptie en vertaling
    return jsonify({
        'transcript': transcript,
        'translated_text': translated_text,
        'audio_url': f'/ai/download_audio/{audio_filename}'
    }), 200

# Functie om audio om te zetten naar tekst via Whisper (de juiste methode)
def transcribe_audio(file_path):
    with open(file_path, "rb") as audio_file:
        transcript_response = client.audio.transcriptions.create(
              model="whisper-1",
              file=audio_file
              )
    
    transcript_text = transcript_response.text
    return transcript_text

# Functie om tekst te vertalen via GPT-4
def translate_text(text, target_language):
    # Gebruik de ChatGPT API voor vertaling
    messages = [
        {"role": "system", "content": f"Je bent een vertaler. Vertaal de volgende tekst naar {target_language}."},
        {"role": "user", "content": text}
    ]

    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
        max_tokens=1000,
        temperature=0.7
    )

    translated_text = response.choices[0].message.content
    return translated_text

@ai_bp.route('/translate', methods=['POST'])
def translate_text_endpoint():
    data = request.get_json()
    text = data.get('text')
    target_language = data.get('target_language', 'en')  # Standaard naar Engels

    # Vertaal de volledige tekst
    translated_text = translate_text(text, target_language)

    # Gebruik OpenAI Text-to-Speech om spraak te genereren van de vertaalde tekst
    audio_filename = text_to_speech_openai(translated_text)

    # Return de vertaalde tekst en de audio-URL
    return jsonify({
        'translated_text': translated_text,
        'audio_url': f'/ai/download_audio/{audio_filename}'  # Stuur de URL van het audiobestand mee
    }), 200

def text_to_speech_openai(text):
    response = client.audio.speech.create(
        model= "tts-1",
        input=text,
        voice="alloy",  # Je kunt hier de juiste stem kiezen
        response_format="mp3"  # MP3-output
    )

    audio_filename = "translated_audio.mp3"
    # Sla het gegenereerde MP3-bestand op
    with open(audio_filename, "wb") as audio_file:
        print(response)
        audio_file.write(response.content)

    return audio_filename

# Route om het gegenereerde audiobestand terug te sturen
@ai_bp.route('/download_audio/<filename>')
def download_audio(filename):
    print(filename)
    return send_file(filename, as_attachment=False)