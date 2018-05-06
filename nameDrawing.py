import random

names_dict = {
    'nh': 'Nate',
    'ml': 'Marlene',
    'lb': 'Liz',
    'jm': 'Doc',
    'kl': 'Kevin',
    'tr': 'Tim',
    'dn': 'Duck'
}


def draw_name(response):
    if type(response) == list:
        return random.choice(response) + " volunteers as tribute!"
    else:
        return "the argument must be a list"


while True:
    playDice = input("Draw a name? (y/n)")
    if playDice == "y":
        print(draw_name(list(names_dict.values())))

