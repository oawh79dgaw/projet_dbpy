import mysql.connector
from datetime import datetime

def open_db():
    return mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="root",
        database="braintraining",
        buffered=True,
        autocommit=True
    )

db_connection = open_db()

def get_excercice(name):
    query = "SELECT id FROM excercices WHERE name = %s"
    cursor = db_connection.cursor()
    cursor.execute(query, (name,))
    row = cursor.fetchone()
    cursor.close()
    return row[0]

def save_result(username, excercice_id, start_date, nb_try, nb_ok):
    date = datetime.now()
    duration = date - start_date
    print(username, excercice_id, datetime.now(), nb_try, nb_ok)
    query = "INSERT INTO results (username, excercice_id, date, duration, nb_try, nb_ok) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor = db_connection.cursor()
    cursor.execute(query, (username, excercice_id, datetime.now(), duration, nb_try, nb_ok,))
    cursor.close()
    return True