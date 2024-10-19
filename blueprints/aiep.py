from flask import Blueprint, request
from ai import aifuncties as aif
ai_bp = Blueprint('ai', __name__)

@ai_bp.route("/aitest")
def lvs_allestudenten():
  return "aitest v2"

@ai_bp.route("/voice", methods=['POST'])
def voice():
  return aif.voice()

@ai_bp.route("/handle-recording", methods=['POST'])
def handle_recording():
  return aif.handle_recording()
  
@ai_bp.route("/brengrecordover/<recid>", methods=['GET'])
def recording_ai_transcript(recid):
  return aif.recording_ai_transcript()

@ai_bp.route("/allerecs", methods=['GET'])
def allerecs():
  return aif.allerecs()
