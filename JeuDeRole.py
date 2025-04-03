import random

player_life = 50
potions = 3
pass_turn = False

ennemi_life = 50

while player_life != 0 or ennemi_life != 0:
    if pass_turn == False:
        choice_input = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")

    if choice_input.isdigit():
        ennemi_attack = random.randint(5, 16)

        if pass_turn == False:
            if int(choice_input) == 1:
                player_attack = random.randint(5, 11)
                ennemi_life -= player_attack
                print(f"Vous avez infligé {player_attack} points de dégats à l'ennemi")
            elif int(choice_input) == 2:
                if potions > 0:
                    random_bonus = random.randint(15, 51)
                    player_life += random_bonus
                    potions -= 1
                    pass_turn = True
                    print(f"Vous récupérez {random_bonus} points de vie ({potions} restantes)")
                else:
                    print("Vous n'avez plus de potions...")
                    continue
            else:
                continue
        else:
            print("Vous passez votre tour...")
            pass_turn = False

        if ennemi_life <= 0:
            print("Tu as gagné !")
            break

        print(f"L'ennemi vous a infligé {ennemi_attack} points de dégats")
        
        player_life -= ennemi_attack

        if player_life <= 0:
            print("Dommage ! Tu as perdu...")
            print(f"Il ne restait que {ennemi_life} points de vie à l'ennemi")
            break

        print(f"Il vous reste {player_life} points de vie")
        print(f"Il reste {ennemi_life} points de vie à l'ennemi")
        print("-----------------------------------------------------")
    else:
        continue

print("Fin du jeu.")
quit()