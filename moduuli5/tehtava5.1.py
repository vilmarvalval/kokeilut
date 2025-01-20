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
lopputulos=0
osoitin=0
while osoitin < len(heitot):
    lopputulos=lopputulos+heitot[osoitin]
    osoitin=osoitin+1
print(f"Yhteensä: {lopputulos}")