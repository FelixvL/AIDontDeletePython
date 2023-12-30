from flask import Flask
from flask_cors import CORS
from flask_cors import cross_origin
import os
from openai import OpenAI
from flask import request
import json


import temporarydefs
import ata_trial_functions

from dotenv import load_dotenv
load_dotenv()

# Set environment variables
os.environ['API_USER'] = 'username'
app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'application/json'

aikey = os.environ.get('ONZEENVKEY')

@app.route("/")
def helloWorld():
  return "Hello, Versie 3"


@app.route("/abc/<invoer>")
def abc(invoer):
  client = OpenAI(api_key=aikey)
  response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[{
        "role": "system",
        "content": ""+invoer
      }],
    temperature=0.5,
    max_tokens=256
  )
  print(response)
  return response.choices[0].message.content

@app.route("/summarizer", methods=['POST'])
def summarizer():
  data_str = request.data.decode('utf-8')

  data_json = json.loads(data_str)

  inputtext = data_json['inhoud']
  print(inputtext)
  return temporarydefs.summarizer(aikey, inputtext)

@app.route("/genereer_afbeelding", methods=['POST'])
def genereer_afbeelding():
  api_key = os.environ.get('ONZEENVKEY')
  data_str = request.data.decode('utf-8')
  data_json = json.loads(data_str)
  inputtext = data_json['inhoud']
  print(inputtext)
  returnString = ata_trial_functions.genereer_afbeelding(api_key, inputtext)
  print(returnString)
  return returnString

@app.route("/genereer_geluid", methods=['POST'])
def genereer_geluid():
  print("ja in geluid")
#  data_str = request.data.decode('utf-8')
  data_json = json.loads(request.data)
  inputtext = data_json['file']
  file_data = base64.b64decode(inputtext.split(',')[1])
  print(inputtext)
      # You might want to add a unique identifier or timestamp to the filename
  filename = 'recording.mp3'
  with open(f"./{filename}", 'wb') as f:
    f.write(file_data)
  return "hoi"
  # if 'file' not in request.files:
  #   return 'No file part', 400
  # file = request.files['file']
  # if file.filename == '':
  #   return 'No selected file', 400
  # if file:
  #   # Process the file as needed, e.g., save it to a directory
  #   file.save("./" + file.filename)
  #   return 'File successfully uploaded', 200
@app.route("/vertaal_audio", methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def go():
  print("go")
  print(request.files)
  file = request.files['file']
  file.save("./" + file.filename)
  from openai import OpenAI

  client = OpenAI(api_key=aikey)

  audio_file = open(file.filename, "rb")
  transcript = client.audio.transcriptions.create(
    model="whisper-1",
    file=audio_file
  )

  print(transcript)

  return transcript.text
@app.route("/vraagstellen", methods=['POST'])
def delaatste():
  data_str = request.data.decode('utf-8')


  data_json = json.loads(data_str)

  inputtext = data_json['inhoud']
  client = OpenAI(api_key=aikey)
  response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[{
        "role": "system",
        "content": ""+inputtext
      }],
    temperature=0.5,
    max_tokens=256
  )
  print(response)
  return response.choices[0].message.content

if __name__ == '__main__':
    app.run(debug=True)
