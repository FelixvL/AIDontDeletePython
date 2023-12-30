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

os.environ['API_USER'] = 'username'
app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'application/json'

aikey = os.environ.get('ONZEENVKEY')

@app.route("/")
def helloWorld():
  return "Hello, Versie 5"


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
  data_json = json.loads(request.data.decode('utf-8'))
  return temporarydefs.summarizer(aikey, data_json['inhoud'])

@app.route("/genereer_afbeelding", methods=['POST'])
def genereer_afbeelding():
  data_json = json.loads(request.data.decode('utf-8'))
  return ata_trial_functions.genereer_afbeelding(aikey, data_json['inhoud'])

@app.route("/vertaal_audio", methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
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
  data_json = json.loads(request.data.decode('utf-8'))
  return ata_trial_functions.simple_chat_completion(aikey, data_json['inhoud'])

@app.route("/krijg_sleutel/<ww>")
def krijg_sleutel(ww):
  if ww == "0111":
    return aikey
  return "nep"

@app.route("/vision")
def vision():
  client = OpenAI(api_key=aikey)

  response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
      {
        "role": "user",
        "content": [
          {"type": "text", "text": "What’s in this image?"},
          {
            "type": "image_url",
            "image_url": {
              "url": "https://aidontdeletepython.azurewebsites.net/static/abc.png",
            },
          },
        ],
      }
    ],
    max_tokens=300,
  )

  print(response.choices[0].message.content)
  return response.choices[0].message.content

@app.route("/afbeelding_online_plaatsen", methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def afbeelding_online_plaatsen():
  print("doe het")
  file = request.files['file']
  print(file)
  file.save("./static/abc.png")
  return "bestandopgeslagen"

if __name__ == '__main__':
    app.run(debug=True)
