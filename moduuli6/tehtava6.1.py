import random

def nopanheitto():
    arvo = random.randint(1, 6)
    return arvo
haluttu = 0
while haluttu != 6:
    haluttu= nopanheitto()
    print(haluttu)