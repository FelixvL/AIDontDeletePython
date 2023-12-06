from flask import Flask
from flask_cors import CORS
import os
import openai

# Set environment variables
os.environ['API_USER'] = 'username'
app = Flask(__name__)
CORS(app)

@app.route("/")
def helloWorld():
  return "Hello, cross-origin-world!"+os.environ.get('ONZEENVKEY')



@app.route("/abc/<invoer>")
def abc(invoer):
  openai.api_key = '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'
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