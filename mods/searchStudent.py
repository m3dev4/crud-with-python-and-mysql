from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv()

secretKey = os.getenv("PASSWORD_DATABASE")


def searchStudent():
    try:
        import mysql.connector

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd=secretKey,
            database="simplon",
        )

        if conn.is_connected():
            print("Connexion réussie à la base de données MySQL")

        connectDb = conn.cursor()
        query = """
            SELECT * FROM students 
        """
        connectDb.execute(query)
        records = connectDb.fetchall()
        nameStudent = input("Entrer le nom de l'apprenant: ").capitalize()
      
        found = False
        for record in records:
            if nameStudent == record[2] or nameStudent == record[1]:
                print(f"Nom: {record[1]}, Prénom: {record[2]}, Promo: {record[3]}")
                found = True
       
        if not found:
            print("Apprenant introuvable")
           

    except Error as e:
        print("Error while connecting to MySQL", e)
