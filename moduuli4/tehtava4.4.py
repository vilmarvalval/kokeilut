import random

numero = 0
oikea = random.randint(1, 6)
while numero != oikea:
    numero = float(input("Arvaa valitsemani numero 1 ja 6 välillä: "))
    if numero < oikea:
        print("Liian pieni arvaus.")
    if numero > oikea:
        print("Liian suuri arvaus.")
    if numero == oikea:
        print("Oikein!")