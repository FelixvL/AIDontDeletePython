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

@ai_bp.route("/voice2", methods=['POST'])
def voice_reply2():
    print("stap1")
    # Creëer een Twilio Voice Response object
    resp = VoiceResponse()

    # Start een opname en laat de beller een bericht inspreken
    resp.say("Hallo! Dit gesprek wordt opgenomen.", voice='alice')

    # Begin de opname
    resp.record(maxLength=60, playBeep=True, action="/ai/handle-recording")

    return str(resp)

# Dit endpoint wordt aangeroepen wanneer de opname klaar is
@ai_bp.route("/handle-recording", methods=['POST'])
def handle_recording():
    recording_url = request.form["RecordingUrl"]
    
    # Hier kun je de opname URL opslaan of verwerken
    print(f"Opname URL: {recording_url}")

    # Bedank de beller en beëindig het gesprek
    resp = VoiceResponse()
    resp.say("Bedankt voor je boodschap. Tot ziens!", voice='alice')
    
    return str(resp)
