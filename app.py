from flask import Flask
from flask_cors import CORS
from flask_cors import cross_origin
from flask import request
from openai import OpenAI
from dotenv import load_dotenv

import os
import json

import temporarydefs
import ata_trial_functions

load_dotenv()

os.environ['API_USER'] = 'username'
app = Flask(__name__)
CORS(app)

aikey = os.environ.get('ONZEENVKEY')

@app.route("/")
def helloWorld():
  return "Hello, Versie 4"


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
  return response.choices[0].message.content

@app.route("/summarizer", methods=['POST'])
def summarizer():
  data_str = request.data.decode('utf-8')
  data_json = json.loads(data_str)
  inputtext = data_json['inhoud']
  return temporarydefs.summarizer(aikey, inputtext)

@app.route("/genereer_afbeelding", methods=['POST'])
def genereer_afbeelding():
  data_str = request.data.decode('utf-8')
  data_json = json.loads(data_str)
  inputtext = data_json['inhoud']
  returnString = ata_trial_functions.genereer_afbeelding(aikey, inputtext)
  return returnString

@app.route("/go", methods=['POST'])
def go():
  file = request.files['file']
  file.save("./" + file.filename)
  client = OpenAI(api_key=aikey)
  audio_file = open(file.filename, "rb")
  transcript = client.audio.transcriptions.create(
    model="whisper-1",
    file=audio_file
  )
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
    temperature=0.9,
    max_tokens=2000
  )
  return response.choices[0].message.content

if __name__ == '__main__':
    app.run(debug=True)
