from flask import Flask
from flask_cors import CORS
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

if __name__ == '__main__':
    app.run(debug=True)
