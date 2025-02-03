tunnus = "python"
salis = "rules"
KysyTunnus = input("Anna käyttäjätunnus: ")
KysySalis = input("Anna salasana: ")
kerrat = 0

while tunnus != KysyTunnus and salis != KysySalis:
    if tunnus != KysyTunnus or salis != KysySalis:
        print("Väärä salasana tai käyttäjätunnus.")
        kerrat = kerrat+1
    if kerrat >= 5:
        break
    KysyTunnus = input("Anna käyttäjätunnus: ")
    KysySalis = input("Anna salasana: ")

if tunnus == KysyTunnus and salis == KysySalis:
    print("Tervetuloa")
else:
    print("Pääsy evätty.")