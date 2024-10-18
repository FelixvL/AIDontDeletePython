from flask import Blueprint, request

# Maak een Blueprint aan
ai_bp = Blueprint('ai', __name__)

from ai import aifuncties as aif

@ai_bp.route("/aitest")
def lvs_allestudenten():
  return "aitest"
