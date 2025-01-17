import random
heitot=[]
arvat=[]
print("Anna arpakuutioiden määrä:")
luku = int(input())
print("Anna arpakuutioiden tahkojen määrä:")
tahkot = int(input())

while luku > 0:
    kuutio = "Noppa "+str(luku)
    arvat.append(kuutio)
    luku = luku-1

print(f"{len(arvat)}:n {tahkot}-tahkoisen arpakuution tulokset:")
for heitto in arvat:
    tulos = random.randint(1, tahkot)
    heitot.append(tulos)

print(heitot)