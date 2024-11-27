exercice.python
def lister_todos():
    print('Fonctionnalité"lister les todos" a venir')

def creer_todo():
    print('Fonctionnalité " créer un todo" à venir')

def modifier_statut_todo():
    print('Fonctionalité " modifier le statut d\'un todo "à venir')

def supprimer_todo():
    print ('Fonctionnalité " supprimer un todo " à venir ')


choix ='' 

while choix != 'q':
    print ('\n==== Menu principal ====')
    print('1:lister les todos')
    print('2:créer un todo')
    print('3:Changer le status d\un todo')
    print('4:Supprimer un todo')
    print('q:quitter')
    print('========================')

    choix= input ('=> Choix:')
    match choix:
        case'1':lister_todos()
        case'2':creer_todos()
        case'3': modifier_status_todo()
        case'4':supprimer_todos()
        case'q':print('Au revoir')
        case_:print('Choix invalide')