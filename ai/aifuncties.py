from twilio.twiml.voice_response import VoiceResponse
import os
import requests
from openai import OpenAI
import mysql.connector

from dotenv import load_dotenv
load_dotenv()

def voice():
  resp = VoiceResponse()
  resp.say("Hello Arjan and Martijn. Tell me your message!", voice='alice')
  resp.record(maxLength=60, playBeep=True, action="/ai/handle-recording")
  return str(resp)

def handle_recording():
  recording_url = request.form["RecordingUrl"]
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
  conn.commit()
  resp = VoiceResponse()
  resp.say("Thanks for you update, see you around!", voice='alice')
  return str(resp)

def recording_ai_transcript():
  account_sid = os.environ.get('TWILIOSID')
  auth_token = os.environ.get('TWILIOAUTH')
  audio_file_path = "opname.mp3"
  recording_url = "https://api.twilio.com/2010-04-01/Accounts/"+os.environ.get('TWILIOSID')+"/Recordings/"+recid
  response = requests.get(f"{recording_url}.mp3", auth=(account_sid, auth_token))

  with open(audio_file_path, "wb") as f:
    f.write(response.content)
  client = OpenAI(api_key=os.environ.get('ONZEENVKEY'))
  audio_file = open(audio_file_path, "rb")
  transcript = client.audio.transcriptions.create(
    model="whisper-1",
    file=audio_file
  )
  return "BERICHT: " + transcript.text

def allerecs():
  conn = mysql.connector.connect(
      host=os.environ.get('ONZEDATABASESERVER'),
      user=os.environ.get('ONZEDATABASEUSER'),
      password=os.environ.get('ONZEDATABASEWACHTWOORD'),
      database="__ai"
  )
  sql = "SELECT * FROM opnamen"
  cursor = conn.cursor()
  cursor.execute(sql)
  resultaten = cursor.fetchall()
  returnstring = ""
  for r in resultaten:
    returnstring += "<a href=\"https://pythonapplicatie-c4fub0d3eqbyc7gt.westeurope-01.azurewebsites.net/ai/brengrecordover/"+r[1].split("/")[7]+"\">"+r[1].split("/")[7]+"</a>"
  return returnstring  
