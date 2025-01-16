tunnus = "python"
salis = "rules"
KysyTunnus = input("Anna käyttäjätunnus: ")
KysySalis = input("Anna salasana: ")

while tunnus != KysyTunnus and salis != KysySalis:
    print("Pääsy evätty.")
    KysyTunnus = input("Anna käyttäjätunnus: ")
    KysySalis = input("Anna salasana: ")

print("Tervetuloa")