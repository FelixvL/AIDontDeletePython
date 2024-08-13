import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()

def maakverbinding():
    conn = mysql.connector.connect(
        host=os.environ.get('ONZEDATABASESERVER'),    # Je hostnaam (bijv. 'localhost')
        user=os.environ.get('ONZEDATABASEUSER'),  # Je MySQL gebruikersnaam
        password=os.environ.get('ONZEDATABASEWACHTWOORD'),  # Je MySQL wachtwoord
        database=os.environ.get('ONZEDATABASE')  # De database waarmee je verbinding wilt maken
    )
    return conn

def voer_select_query_uit(sqlquery):
    c = maakverbinding()
    cursor = c.cursor()
    cursor.execute(sqlquery)
    resultaten = cursor.fetchall()
    return resultaten, cursor

def voer_insert_query_uit(insertquery, valueparen):
    c = maakverbinding()
    cursor = c.cursor()
    sql = insertquery
    val = valueparen
    cursor.execute(sql, val)
    return c.commit()

def zet_om_naar_json(record_set, cursor):
    keys = [i[0] for i in cursor.description]

    data = [
        dict(zip(keys, row)) for row in record_set
    ]
    return data

def alle_studenten():
    r,c = voer_select_query_uit("SELECT * FROM student")
    return zet_om_naar_json(r,c)
    

def toon_alle_lesstofitems():
    r,c = voer_select_query_uit("SELECT * FROM lesstofitem")
    return zet_om_naar_json(r,c)

def docent_alle_trajecten():
    r,c = voer_select_query_uit("SELECT * FROM traject")
    return zet_om_naar_json(r,c)

def docent_alle_lesstofitems_per_traject(traject_id):
    r,c = voer_select_query_uit(f"""SELECT 
    l.naam AS lesstofitemnaam,
    l.id AS lesstofitemid,
    CASE 
        WHEN tl.id IS NOT NULL THEN 'checked'
        ELSE ''
    END AS statustraject
FROM 
    lesstofitem l
LEFT JOIN 
    traject_lesstofitem tl ON l.id = tl.lesstofitem_id AND tl.traject_id = {traject_id}
ORDER BY 
    l.naam;
""")
    return zet_om_naar_json(r,c)

def student_alle_lesstofitems_per_traject(student_id):
    r,c = voer_select_query_uit("SELECT * FROM student WHERE student.id = "+student_id)
    print(r)
    print(r[0])
    print(r[0][2])
    r,c = voer_select_query_uit("""SELECT 
    l.naam AS lesstofitemnaam,
    l.id AS lesstofitemid,
    CASE 
        WHEN sli.id IS NOT NULL THEN 'checked'
        ELSE ''
    END AS statusstudent
FROM 
    student s
JOIN 
    traject t ON s.traject_id = t.id
JOIN 
    traject_lesstofitem tl ON tl.traject_id = t.id
JOIN 
    lesstofitem l ON l.id = tl.lesstofitem_id
LEFT JOIN 
    student_lesstofitem sli ON sli.lesstofitem_id = l.id AND sli.student_id = s.id
WHERE 
    t.id = """+str(r[0][2]))
    return zet_om_naar_json(r,c)

def docent_ken_lesstofitem_toe_aan_traject(traject_id,lesstofitem_id):
    print(traject_id, " go ", lesstofitem_id)
    r = voer_insert_query_uit("INSERT INTO traject_lesstofitem (traject_id, lesstofitem_id) VALUES (%s, %s)",(traject_id,lesstofitem_id))
    print(r)
    return '{"yes":"docent_ken_lesstofitem_toe_aan_traject"}'

def student_ken_lesstofitem_toe_aan_student(student_id, lesstofitem_id):
    print(student_id, " jo ", lesstofitem_id)
    r = voer_insert_query_uit("INSERT INTO student_lesstofitem (student_id, lesstofitem_id) VALUES (%s, %s)",(student_id,lesstofitem_id))
    print(r)
    return '{"yes":"student_ken_lesstofitem_toe_aan_student"}'   

def docent_maak_lesstofitem_aan(data):
    r = voer_insert_query_uit("INSERT INTO lesstofitem (naam, inhoud) VALUES (%s, %s)",(data.get('lsi_titel'), data.get('lsi_titel')))
    return '{"yes":"docent_maak_lesstofitem_aa"}' 