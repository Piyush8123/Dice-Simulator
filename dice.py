import random

i = "Y"

while i == "Y":
    n = random.randint(1, 6)
    if n == 1:
        print("----------")
        print("|        |")
        print("|    O   |")
        print("|        |")
        print("----------")

    if n == 2:
        print("----------")
        print("|        |")
        print("| O    O |")
        print("|        |")
        print("----------")

    if n == 3:
        print("----------")
        print("|    O   |")
        print("|    O   |")
        print("|    O   |")
        print("----------")

    if n == 4:
        print("----------")
        print("| O    O |")
        print("|        |")
        print("| O    O |")
        print("----------")

    if n == 5:
        print("----------")
        print("| O    O |")
        print("|    O   |")
        print("| O    O |")
        print("----------")

    if n == 6:
        print("----------")
        print("| O    O |")
        print("| O    O |")
        print("| O    O |")
        print("----------")

    i = input("Enter Y to continue and N to finish the game : ")

else:
    print("Thanks for playing the game!!")