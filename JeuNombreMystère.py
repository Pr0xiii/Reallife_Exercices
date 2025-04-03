import random

def getRandomNumber():
    max_essai = 5
    current_essai = max_essai
    nombre_mystere = random.randint(0, 101)
    while current_essai != 0:
        print(f"Il te reste {current_essai} essais")
        input_number = input("Devine le nombre : ")

        if input_number.isdigit():
            current_essai -= 1
            if int(input_number) == nombre_mystere:
                print(f"Bravo ! Le nombre mystère était bien {nombre_mystere}")
                print(f"Tu as trouvé le nombre en {max_essai - current_essai} essai")
                print("Fin du jeu")
                quit()
                break
            else:
                if nombre_mystere < int(input_number):
                    print(f"Le nombre mystère est plus petit que {int(input_number)}")
                else:
                    print(f"Le nombre mystère est plus grand que {int(input_number)}")
        else:
            print("Veuillez entrer un nombre valide")

    print(f"Dommage ! Le nombre mystère était {nombre_mystere}")
    print("Fin du jeu")
    quit()

print("*** Le jeu du nombre mystère ***")
getRandomNumber()