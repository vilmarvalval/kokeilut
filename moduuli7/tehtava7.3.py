lentoasema= {}

#lentoaseman lisääminen sanakirjaan.
def anto():
    koodi=""
    while koodi =="":
        print("↘")
        print(" Syötä lentoaseman ICAO-koodi:")
        koodi = input(" ").upper()
        if koodi !="":
            lentoasema[koodi]= None
        elif koodi.lower() == "poistu":
            print("↙")
            break
        else:
            print(" Virheellinen syöte.")
    nimi=""
    while nimi=="" and koodi.lower() !="poistu":
        print(" ↓")
        print(" Syötä lentoaseman nimi:")
        nimi=input(" ")
        if nimi !="":
            lentoasema[koodi]= nimi
            print(" Lentoasema lisätty.")
            print("↙")
        elif nimi.lower() == "poistu":
            print("↙")
            break
        else:
            print(" Virheellinen syöte.")

#lentokentän hakeminen sanakirjasta.
def haku():
    print("↘")
    print(f" {len(lentoasema)} lentoasemaa tietokannassa.")
    if len(lentoasema) == 0:
        print(" Et ole vielä syöttänyt yhtäkään lentoasemaa.")
        print("↙")
    else:
        print(" Anna lentoaseman ICAO-koodi")
        koodi = input(" ").upper()
        if koodi in lentoasema:
            print(f" {koodi} on {lentoasema[koodi]}")
            print("↙")
        elif koodi.lower() == "poistu":
            print("↙")
        else:
            print(" Lentoasemaa ei löytynyt.")
            print("↙")


print("Tämä on lentoasematietojen haku ja tallennus ohjelma.")
print("Sallitut komennot:")
print("'Uusi' syöttää uuden lentoaseman.")
print("'Hae' hakee jo syötettyjen lentoasemien joukusta.")
print("'poistu' palataksesi takaisinpäin tai poistuaksesi.")

while True:
    print("Syötä komento:")
    komento=input().lower()
    if komento == "uusi":
        anto()
    elif komento == "hae":
        haku()
    elif komento == "poistu":
        break
    else:
        print("Virheellinen syöte.")
        print("Sallitut komennot:")
        print("'Uusi' syöttää uuden lentoaseman.")
        print("'Hae' hakee jo syötettyjen lentoasemien joukusta.")
        print("'lopeta' lopettaa ohjelman, voit kirjoittaa tämän milloin vain.")