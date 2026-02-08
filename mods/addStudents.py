import os
from dotenv import load_dotenv

from mysql.connector import Error


load_dotenv()

secretKey = os.getenv("PASSWORD_DATABASE")

"""
    Fonction qui permet d'ajouter un student dans la base de données
    ----------------------------------
    @param nom: Nom de l'apprenant
    @param prenom: Prenom de l'apprenant
    @param promo: Promo de l'apprenant
    ----------------------------------
"""


def addStudents(nom, prenom, promo):
    import mysql.connector

    try:
        # Etablir la connexion avec la base de donnée
        conn = mysql.connector.connect(
            host="localhost", user="root", database="simplon", password=secretKey
        )

        # Verification du connection entre python & le database
        if conn.is_connected():
            print("Connexion réussie à la base de données MySQL")

        executCommand = conn.cursor()
        query = "INSERT INTO students (nom, prenom, promo) VALUES (%s, %s, %s)"
        executCommand.execute(query, (nom, prenom, promo))
        conn.commit()
        print("Apprenant ajouté avec succès")
    except Error as e:
        print(f"Erreur lors de la connexion à MySQL: {e}")
