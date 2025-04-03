choices = ["Choisissez parmi les 5 options suivantes :", "Ajouter un élément à la liste", 
           "Retirer un élément à la liste", "Afficher la liste",
           "Vider la liste", "Quitter"]

current_course_list = []

def onReceivedChoice(choice):
    choice = int(choice)

    if choice == 1:
        element = input("Entrez le nom d'un élément à ajouter à la liste de course : ")
        element = element.lower()
        element = element.capitalize()
        if not element in current_course_list:
            current_course_list.append(element)
            print(f"L'élement {element} a bien été ajouté a la liste.")
        else:
            print(f"L'élément {element} est déjà présent dans la liste de course.")
    elif choice == 2:
        element = input("Entrez le nom d'un élément à retirer de la liste de course : ")
        element = element.lower()
        element = element.capitalize()
        if element in current_course_list:
            current_course_list.remove(element)
            print(f"L'élement {element} a bien été supprimé a la liste.")
        else:
            print(f"L'élément {element} n'est pas dans la liste.")
    elif choice == 3:
        if len(current_course_list) == 0:
            print("Votre liste ne contient aucun élément.")
        else:
            for i, nom in enumerate(current_course_list):
                print(f"{i + 1}. {nom}")
    elif choice == 4:
        current_course_list.clear()
        print("La liste a été vidée de son contenu.")
    elif choice == 5:
        print("A bientôt !")
        quit()
        

    print("-----------------------------------------")
    print_choices()



def print_choices():
    for i, choice in enumerate(choices):
        if i == 0:
            print(choice)
        else:
            print(f"{i}: {choice}")
    choice_input = input("Votre choix : ")
    onReceivedChoice(choice_input)
    
print_choices()
