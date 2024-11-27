# Liste pour stocker les todos sous forme de dictionnaires
todos = []


# Fonction pour lister les todos avec leur statut
def lister_todos():
    if not todos:  # Vérifie si la liste est vide
        print("Aucune tâche à afficher.")
    else:
        print("\n=== Liste des tâches ===")
        for i, todo in enumerate(todos, 1):
            print(f"{i}. {todo['titre']} - Statut : {todo['statut']}")


# Fonction pour créer un nouveau todo
def creer_todo():
    titre = input("Entrez le titre de la tâche : ")
    todos.append({"titre": titre, "statut": "À faire"})  # Statut par défaut : "À faire"
    print(f"Tâche '{titre}' ajoutée avec le statut 'À faire'.")


# Fonction pour basculer le statut d'un todo
def basculer_statut_todo():
    if not todos:  # Vérifie si la liste est vide
        print("Aucune tâche à modifier.")
        return

    # Lister les todos pour choisir
    print("\n=== Basculer le statut d'une tâche ===")
    lister_todos()

    try:
        choix = int(input("Entrez le numéro de la tâche à modifier : "))
        if 1 <= choix <= len(todos):  # Vérifie si le choix est valide
            todo = todos[choix - 1]  # Récupère la tâche sélectionnée
            print(f"Tâche sélectionnée : {todo['titre']} (Statut actuel : {todo['statut']})")

            # Basculement du statut
            if todo["statut"] == "À faire":
                todo["statut"] = "Fait"
                print(f"Le statut de la tâche '{todo['titre']}' est maintenant 'Fait'.")
            elif todo["statut"] == "Fait":
                todo["statut"] = "À faire"
                print(f"Le statut de la tâche '{todo['titre']}' est maintenant 'À faire'.")
        else:
            print("Numéro invalide.")
    except ValueError:
        print("Veuillez entrer un numéro valide.")


# Fonction pour supprimer un todo
def supprimer_todo():
    if not todos:  # Vérifie si la liste est vide
        print("Aucune tâche à supprimer.")
        return

    # Lister les todos pour choisir
    print("\n=== Supprimer une tâche ===")
    lister_todos()

    try:
        choix = int(input("Entrez le numéro de la tâche à supprimer : "))
        if 1 <= choix <= len(todos):  # Vérifie si le choix est valide
            todo = todos.pop(choix - 1)  # Supprime la tâche choisie
            print(f"Tâche '{todo['titre']}' supprimée.")
        else:
            print("Numéro invalide.")
    except ValueError:
        print("Veuillez entrer un numéro valide.")


# Menu principal
choix = ""
while choix != "q":
    # Affichage des choix
    print("\n=== Menu principal ===")
    print("1: Lister les todos")
    print("2: Créer un todo")
    print("3: Modifier le statut d'un todo")
    print("4: Supprimer un todo")
    print("q: Quitter")

    # Actions suivant le choix
    choix = input(">>> Choix : ")
    match choix:
        case "1":
            lister_todos()
        case "2":
            creer_todo()
        case "3":
            basculer_statut_todo()
        case "4":
            supprimer_todo()
        case "q":
            print("Au revoir")
        case _:
            print("Choix invalide.")