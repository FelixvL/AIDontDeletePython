from flask import Blueprint, request
from twilio.twiml.voice_response import VoiceResponse
import os
import requests
from openai import OpenAI
import mysql.connector

from dotenv import load_dotenv
load_dotenv()

# Maak een Blueprint aan
ai_bp = Blueprint('ai', __name__)

from ai import aifuncties as aif

@ai_bp.route("/aitest")
def lvs_allestudenten():
  return "aitest v1"


@ai_bp.route("/voice", methods=['POST'])
def voice_reply():
  resp = VoiceResponse()
  # Geef een gesproken boodschap terug
  resp.say("Hello? Thanks for calling, tell us your story", voice='alice')
  return str(resp)

@ai_bp.route("/voice2", methods=['POST'])
def voice_reply2():
  print("stap1")
  # Creëer een Twilio Voice Response object
  resp = VoiceResponse()

  # Start een opname en laat de beller een bericht inspreken
  resp.say("Hello Arjan and Martijn. Tell me your message!", voice='alice')

  # Begin de opname
  resp.record(maxLength=60, playBeep=True, action="/ai/handle-recording")

  return str(resp)

# Dit endpoint wordt aangeroepen wanneer de opname klaar is
@ai_bp.route("/handle-recording", methods=['POST'])
def handle_recording():
  recording_url = request.form["RecordingUrl"]
  
  # Hier kun je de opname URL opslaan of verwerken
  print(f"Opname URL: {recording_url}")
  conn = mysql.connector.connect(
      host=os.environ.get('ONZEDATABASESERVER'),    # Je hostnaam (bijv. 'localhost')
      user=os.environ.get('ONZEDATABASEUSER'),  # Je MySQL gebruikersnaam
      password=os.environ.get('ONZEDATABASEWACHTWOORD'),  # Je MySQL wachtwoord
      database="__ai"  # De database waarmee je verbinding wilt maken
  )
  sql = "INSERT INTO opnamen (opname_id, telefoonnr) VALUES (%s, %s)"
  val = (recording_url, "0615517962")
  cursor = conn.cursor()
  cursor.execute(sql, val)
  c.commit()
  # Bedank de beller en beëindig het gesprek
  resp = VoiceResponse()
  resp.say("Thanks for you update, see you around!", voice='alice')
  
  return str(resp)

@ai_bp.route("/brengrecordover/<recid>", methods=['GET'])
def brengrecordover(recid):
  account_sid = os.environ.get('TWILIOSID')
  auth_token = os.environ.get('TWILIOAUTH')

  # De URL van de opname die je wilt downloaden
  recording_url = "https://api.twilio.com/2010-04-01/Accounts/"+os.environ.get('TWILIOSID')+"/Recordings/"+recid
  
  response = requests.get(f"{recording_url}.mp3", auth=(account_sid, auth_token))

  with open("opname.mp3", "wb") as f:
    f.write(response.content)

  # Je OpenAI API-sleutel

  # Pad naar het MP3-bestand dat je wilt omzetten
  audio_file_path = "opname.mp3"

# Open het MP3-bestand
  client = OpenAI(api_key=os.environ.get('ONZEENVKEY'))
  audio_file = open("opname.mp3", "rb")
  transcript = client.audio.transcriptions.create(
    model="whisper-1",
    file=audio_file
  )


# De getranscribeerde tekst weergeven
  print(transcript.text)

  return "breng record over gelukt" + transcript.text


