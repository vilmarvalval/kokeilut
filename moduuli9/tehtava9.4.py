import random

autot= []
#Tehdään Auto luokka jolle annetaan mahdolliset ominaisuudet ovat huippunopeus, nykynopeus, kuljettu matka ja rekkari.
class Auto:
    nyky_kmh = 0
    trippi_mit = 0
    def __init__(self, rekkari, huippu_kmh):
        self.rekkari = rekkari
        self.huippu_kmh = huippu_kmh
    #Tämä funktio tulostaa kaikki auton ominaisuudet ja niiden nykyiset arvot.
    def ominaisuudet(self):
        print(f"Rekkari: {self.rekkari}\n"
              f"Huippunopeus: {self.huippu_kmh}kmh\n"
              f"Nykynopeus: {self.nyky_kmh}kmh\n"
              f"Kuljettu matka: {self.trippi_mit}km")

    #Tämän funktion avulla auto saadaan kiihdyttämään.
    # Kiihdytyksen jälkeen funktio katsoo, onko nopeus mennyt yli auton huippunopeuden tai alle nollan.
    # Jos on, niin se korjaa nopeuden maksimiin tai negatiivisen tapauksessa nollaan.
    def kiihdytys(self, nopeusmuutos):
        self.nyky_kmh += float(nopeusmuutos)
        if self.nyky_kmh > self.huippu_kmh:
            self.nyky_kmh = self.huippu_kmh
        if self.nyky_kmh < 0:
            self.nyky_kmh = 0
    #Tämän funktion avulla auto liikkuu
    def kulje(self, aika):
        self.trippi_mit += float(aika)*self.nyky_kmh

monta_autoa = 10 #int(input("Kuinka monta autoa haluat kisaan?: "))
kesto = int(input("Kuinka monta tuntia kisa kestää?: "))

i=0
while monta_autoa > 0:
    i +=1
    #tehdään auto jonka rekisteri on ABC-i ja huippunopeus on satunnainen luku väliltä 100 ja 200kmh
    autot.append(Auto(f"ABC-{i}", random.randint(100, 200)))
    monta_autoa -= 1

print("Kisa alkakoon!")

while kesto > 0:
    for i in autot:

        i.kiihdytys(random.randint(-10, 15))
        i.kulje(1)
    kesto -= 1

autot.sort(key=lambda x: x.trippi_mit, reverse=True)
sija = 0
print()
print("Voittaja:")
for i in autot:
    sija +=1
    print(f"Sija: {sija}.")
    print(i.rekkari)
    print(f"Nopeus: {int(i.nyky_kmh)}kmh")
    print(f"Kuljettu matka: {int(i.trippi_mit)}km")
    print()