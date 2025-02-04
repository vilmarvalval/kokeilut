nimet=set()
def tarkastus(x):
    if x != ":":
        if x in nimet:
            print("Aiemmin syötetty nimi.")
        else:
            print("Uusi nimi.")
        nimet.add(x)

print("Anna nimi tai lopeta painamalla enter.")
nimi = input()

while nimi != "":
    tarkastus(nimi)
    print("Anna nimi tai lopeta painamalla enter.")
    nimi = input()

for i in nimet:
    print(i)