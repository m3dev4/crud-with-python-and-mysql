from mods.addStudents import addStudents
from mods.markPresentStudents import markPresent
from mods.listPresence import listPresence
from mods.searchStudent import searchStudent


def menu():
    print("Bienvenue sur Simplon")
    while True:
        print(
            "Que voulez vous faire:\n 1: Ajouter un apprenant \n 2: Enregistrer la présence pour la séance du jour \n 3: Afficher les apprenants présents \n 4: Rechercher un apprenant"
        )

        choix = input("choix entre 1 et 4: ")

        match choix:
            case "1":
                addStudents( input("Nom: ").capitalize(), input("Prenom: ").capitalize(), input("Promo: ").capitalize())
            case "2":
                markPresent()
            case "3":
                listPresence()
            case "4":
                searchStudent()
            case _:
                print("Choisissez une valeur entre 1 et 4")
        break


if __name__ == "__main__":
    menu()
