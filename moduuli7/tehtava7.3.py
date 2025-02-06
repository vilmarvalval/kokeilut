#Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti,
# kunnes hän haluaa lopettaa. (ICAO-koodi on lentoaseman yksilöivä tunniste.
# Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät koodeja helposti selaimen avulla.)

lentoasema= {}

def anto():
    koodi=""
    while koodi =="":
        print("Syötä lentoaseman ICAO-koodi:")
        koodi = input().upper()
        if koodi !="":
            lentoasema[koodi]= None
        elif koodi.lower() == "poistu":
            break
        else:
            print("Virheellinen syöte.")
    nimi=""
    while nimi=="" and koodi.lower() !="poistu":
        print("Syötä lentoaseman nimi:")
        nimi=input()
        if nimi !="":
            lentoasema[koodi]= nimi
            print("Lentoasema lisätty.")
        elif nimi.lower() == "poistu":
            break
        else:
            print("Virheellinen syöte.")

def haku():
    print(f"{len(lentoasema)} lentoasemaa tietokannassa.")
    if len(lentoasema) == 0:
        print("Et ole vielä syöttänyt yhtäkään lentoasemaa.")
    else:
        print("Anna lentoaseman ICAO-koodi")
        koodi = input().upper()
        if koodi in lentoasema:
            print(f"{koodi} on {lentoasema[koodi]}")
        if koodi.lower() == "poistu":
            print()
        else:
            print("Lentoasemaa ei löytynyt.")

on=True

print("Tämä on lentoasematietojen haku ja tallennus ohjelma.")
print("Sallitut komennot:")
print("'Uusi' syöttää uuden lentoaseman.")
print("'Hae' hakee jo syötettyjen lentoasemien joukusta.")
print("'poistu' palataksesi takaisinpäin tai poistuaksesi.")

while on:
    print("Syötä komento:")
    komento=input().lower()
    if komento == "uusi":
        anto()
    elif komento == "hae":
        haku()
    elif komento == "poistu":
        break
    else:
        print("Väärä komento")
        print("Sallitut komennot:")
        print("'Uusi' syöttää uuden lentoaseman.")
        print("'Hae' hakee jo syötettyjen lentoasemien joukusta.")
        print("'lopeta' lopettaa ohjelman, voit kirjoittaa tämän milloin vain.")