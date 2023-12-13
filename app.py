from flask import Flask
from flask_cors import CORS
import os
import openai
import temporarydefs
from flask import request
import json


from dotenv import load_dotenv
load_dotenv()

# Set environment variables
os.environ['API_USER'] = 'username'
app = Flask(__name__)
CORS(app)

aikey = os.environ.get('ONZEENVKEY')

@app.route("/")
def helloWorld():
  return "Hello, cross-origin-world!"


@app.route("/abc/<invoer>")
def abc(invoer):
  openai.api_key = os.environ.get('ONZEENVKEY')
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{
        "role": "system",
        "content": ""+invoer
      }],
    temperature=0.5,
    max_tokens=256
  )
  return response["choices"][0]["message"]["content"]

@app.route("/summarizer", methods=['POST'])
def summarizer():
  data_str = request.data.decode('utf-8')

  data_json = json.loads(data_str)

  inputtext = data_json['inhoud']
  print(inputtext)
  return temporarydefs.summarizer(aikey, inputtext)