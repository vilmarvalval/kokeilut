kaupungit=[]

while len(kaupungit) < 5:
    for i in range(0,5):
        print("Anna kaupungin nimi: ")
        kaupunki = input()
        if kaupunki != "":
            kaupungit.append(kaupunki)
        if len(kaupungit) == 5:
            break

print("Annetut kaupungit: ")
for n in kaupungit:
    print(n)