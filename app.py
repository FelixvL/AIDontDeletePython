from flask import Flask
from flask_cors import CORS
import os

# Set environment variables
os.environ['API_USER'] = 'username'
app = Flask(__name__)
CORS(app)

@app.route("/")
def helloWorld():
  return "Hello, cross-origin-world!"+os.environ.get('ONZEENVKEY')