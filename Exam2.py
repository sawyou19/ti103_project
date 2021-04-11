import random

"""
Question 2
"""
a = random.randint(1,3)
print(a)


"""
Question 3
"""
def question_3():
    a = 0

    while True:
        a = input("Entrez un nombre entier entre 1 et 3: ")

        if a.isnumeric():
            a = int(a)
            if a == 1:
                break
            elif a == 2:
                break
            elif a == 3:
                break
            else:
                print("Erreur.")

        else:
            print("Erreur.")

    return a

"""
Question 4
"""
def question_4(porte, choix):
    liste  = 0

    if porte == 1:
        if choix == 1:
            liste = random.randint(2, 3)

        elif choix == 2:
            liste = 3

        elif choix == 3:
            liste = 2

    elif porte == 2:
        if choix == 1:
            liste = 3

        elif choix == 2:
            liste = random.choice([1, 3])

        elif choix == 3:
            liste = 1

    elif porte == 3:
        if choix == 1:
            liste = 2

        elif choix == 2:
            liste = 1

        elif choix == 3:
            liste = random.choice([1, 2])

    print("On ouvre la porte: ", liste)
    return liste


def question_5(choix, ouverte):
    change = input("Conservez vous votre choix (0) ou changez vous votre choix (1)")
    change = int(change)

    if change == 0:
        return choix

    if ouverte == 1:
        if choix == 2:
            return 3

        elif choix == 3:
            return 2

    elif ouverte == 2:
        if choix == 1:
            return 3

        elif choix == 3:
            return 1

    elif ouverte == 3:
        if choix == 1:
            return 2

        elif choix == 2:
            return 1


def question_6(a, new_choix):
    if a == new_choix:
        print("Gagne!")

    else:
        print("Perdu")


"""
Question 7
"""
choix = question_3()
ouverte = question_4(a, choix)
new_choix = question_5(choix, ouverte)
question_6(a, new_choix)




def question_8(choix, ouverte):
    change = input("Conservez vous votre choix (0) ou changez vous votre choix (1)")
    change = int(change)

    if change == 0:
        return choix

    if ouverte == 1:
        if choix == 2:
            return 3

        elif choix == 3:
            return 2

    elif ouverte == 2:
        if choix == 1:
            return 3

        elif choix == 3:
            return 1

    elif ouverte == 3:
        if choix == 1:
            return 2

        elif choix == 2:
            return 1