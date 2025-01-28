import random
tahkot = 0
while tahkot <2:
    print("Anna tahkojen määrä")
    tahkot = int(input())
    if tahkot >= 2:
        break
    else:
        print("Ei voi heittää noppaa jossa on alle 2 tahkoa.")


def nopanheitto():
    arvo = random.randint(1, tahkot)
    return arvo
haluttu = 0
kerrat = 0
while haluttu != tahkot:
    haluttu= nopanheitto()
    kerrat = kerrat+1
    print(haluttu)
print(f"Heitetty {kerrat} kertaa.")