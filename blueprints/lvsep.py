from flask import Blueprint, request

# Maak een Blueprint aan
lvs_bp = Blueprint('lvs', __name__)

from lvs import lesstofitems as li

@lvs_bp.route("/allelesstofitems")
def lvs_allestudenten():
  return li.toon_alle_lesstofitems()

@lvs_bp.route("/alle_studenten")
def alle_studenten():
  return li.alle_studenten()
@lvs_bp.route("/docent_alle_trajecten")
def lvs_docent_alle_trajecten():
  return li.docent_alle_trajecten()

@lvs_bp.route("/docent_alle_lesstofitems_per_traject/<traject_id>")
def lvs_docent_alle_lesstofitems_per_traject(traject_id):
  return li.docent_alle_lesstofitems_per_traject(traject_id)

@lvs_bp.route("student_alle_lesstofitems_per_traject/<student_id>")
def lvs_student_alle_lesstofitems_per_traject(student_id):
  return li.student_alle_lesstofitems_per_traject(student_id)

@lvs_bp.route("docent_ken_lesstofitem_toe_aan_traject/<traject_id>/<lesstofitem_id>")
def lvs_docent_ken_lesstofitem_toe_aan_traject(traject_id,lesstofitem_id):
  return li.docent_ken_lesstofitem_toe_aan_traject(traject_id,lesstofitem_id)

@lvs_bp.route("student_ken_lesstofitem_toe_aan_student/<student_id>/<lesstofitem_id>")
def student_ken_lesstofitem_toe_aan_student(student_id, lesstofitem_id):
  return li.student_ken_lesstofitem_toe_aan_student(student_id, lesstofitem_id)

@lvs_bp.route('docent_maak_lesstofitem_aan', methods=['POST'])
def docent_maak_lesstofitem_aan():
  return li.docent_maak_lesstofitem_aan(request.get_json())
