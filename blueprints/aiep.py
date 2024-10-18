from flask import Blueprint, request
from twilio.twiml.voice_response import VoiceResponse

# Maak een Blueprint aan
ai_bp = Blueprint('ai', __name__)

from ai import aifuncties as aif

@ai_bp.route("/aitest")
def lvs_allestudenten():
  return "aitest"


@ai_bp.route("/voice", methods=['POST'])
def voice_reply():
    resp = VoiceResponse()
    # Geef een gesproken boodschap terug
    resp.say("Hallo! Bedankt dat je belt. Hoe kan ik je helpen?", voice='alice')
    return str(resp)
