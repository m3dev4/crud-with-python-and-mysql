import os
from dotenv import load_dotenv
from mysql.connector import Error


load_dotenv()

secretKey = os.getenv("PASSWORD_DATABASE")


def markPresent():
    import mysql.connector

    try:
        conn = mysql.connector.connect(
            host="localhost", user="root", database="simplon", password=secretKey
        )
        if conn.is_connected():
            print("Connexion réussie à la base de données MySQL")
            
        executeCommand = conn.cursor()
        query = "SELECT * FROM students"
        executeCommand.execute(query)
        records = executeCommand.fetchall()
        #on parcour chaque apprenant pour le marquer oui ou non concernant sa presence
        for row in records:
            print(f"{row[2]} {row[1]} ")
            present = input("Présent ? (oui/non): ")
            if present.lower() == "oui":
                query = "UPDATE students SET is_present = 1 WHERE id = %s"
                executeCommand.execute(query, (row[0],))
                conn.commit()
                print("Les apprenants sont enregistré avec succées")
            else:
                query = "UPDATE students SET is_present = 0 WHERE id = %s"
                executeCommand.execute(query, (row[0],))
                conn.commit()

    except Error as e:
        print(f"Erreur lors de la connexion à MySQL: {e}")
