import random
import math
import test_import

num = random.randint(0,1000)
play = True

print(num)

print(test_import.ma_variable)

while play:
    guess = input("Devinez un nombre entre 1 et 1000 ou 'q' pour quitter: ")

    if guess == 'q':
        break
    elif not guess.isnumeric():
        print("Vous devez entrer un numbre entier.")
    elif int(guess) < 1:
        print("Entre un nombre plus grand ou egal a 1")
    elif int(guess) > 1000:
        print("Entre un nombre plus petit ou egal a 1000")
    elif int(guess) < num:
        print("Plus grand")
    elif int(guess) > num:
        print("Plus petit")
    else:
        print("Tu l'as eu!")
        break

