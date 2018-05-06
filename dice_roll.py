# Author: nhascup
# 05/05/2018
# Python Refresh

import random


def dice_roll():
    return str(random.randint(1, 7))


while True:
    playDice = input("Roll the dice? (y/n)")
    if playDice == "y":
        r1 = str(dice_roll())
        r2 = str(dice_roll())
        print(r1 + " " + r2)
        if r1 == r2:
            print("Doubles!")
    else:
        print("Quitter")
        break
