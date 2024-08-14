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

@lvs_bp.route("/docent_alle_lesstofitems_per_traject/<traject_id>/<zoekterm>")
def lvs_docent_alle_lesstofitems_per_traject(traject_id, zoekterm):
  return li.docent_alle_lesstofitems_per_traject(traject_id, zoekterm)

@lvs_bp.route("/docent_alle_definities/<zoekterm>")
def lvs_docent_alle_definities(zoekterm):
  return li.docent_alle_definities(zoekterm)

@lvs_bp.route("student_alle_lesstofitems_per_traject/<student_id>/<zoekterm>")
def lvs_student_alle_lesstofitems_per_traject(student_id, zoekterm):
  return li.student_alle_lesstofitems_per_traject(student_id, zoekterm)

@lvs_bp.route("docent_ken_lesstofitem_toe_aan_traject/<traject_id>/<lesstofitem_id>")
def lvs_docent_ken_lesstofitem_toe_aan_traject(traject_id,lesstofitem_id):
  return li.docent_ken_lesstofitem_toe_aan_traject(traject_id,lesstofitem_id)

@lvs_bp.route("student_ken_lesstofitem_toe_aan_student/<student_id>/<lesstofitem_id>")
def student_ken_lesstofitem_toe_aan_student(student_id, lesstofitem_id):
  return li.student_ken_lesstofitem_toe_aan_student(student_id, lesstofitem_id)

@lvs_bp.route('docent_maak_lesstofitem_aan', methods=['POST'])
def docent_maak_lesstofitem_aan():
  return li.docent_maak_lesstofitem_aan(request.get_json())

@lvs_bp.route('docent_maak_definitie_aan', methods=['POST'])
def docent_maak_definitie_aan():
  return li.docent_maak_definitie_aan(request.get_json())

@lvs_bp.route('inloggen/<wachtwoord>')
def inloggen(wachtwoord):
  return li.inloggen(wachtwoord)

@lvs_bp.route('inhoud_lesstofitem/<lsid>')
def inhoud_lesstofitem(lsid):
  return li.inhoud_lesstofitem(lsid)
  
@lvs_bp.route('maak_traject_aan/<trajectnaam>')
def maak_traject_aan(trajectnaam):
  return li.maak_traject_aan(trajectnaam)

@lvs_bp.route('maak_student_aan/<studentnaam>')
def maak_student_aan(studentnaam):
  return li.maak_student_aan(studentnaam)


@lvs_bp.route('kies_traject')
def kies_traject():
  return li.docent_alle_trajecten()

@lvs_bp.route('koppel_traject/<tid>/<sid>')
def koppel_traject(tid, sid):
  return li.koppel_traject(tid, sid)

@lvs_bp.route('heeft_student_traject/<sid>')
def heeft_student_traject(sid):
  return li.heeft_student_traject(sid)


