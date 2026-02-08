import os
from dotenv import load_dotenv
from mysql.connector import Error

load_dotenv()

secretKey = os.getenv("PASSWORD_DATABASE")


def listPresence():
    import mysql.connector

    conn = mysql.connector.connect(
        host="localhost", user="root", database="simplon", password=secretKey
    )
    if conn.is_connected():
        print("Connexion réussie à la base de données MySQL")

    executcommand = conn.cursor()
    query = "SELECT * FROM students WHERE is_present = 1"
    executcommand.execute(query)
    listPresence = executcommand.fetchall()
    for presence in listPresence:
        if presence:
            print(f"Nom: {presence[1]}, Prénom: {presence[2]}, Promo: {presence[3]}")
        else:
            print("Aucun apprenant presentes")
            
