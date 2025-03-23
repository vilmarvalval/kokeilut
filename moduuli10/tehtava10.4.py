# jonka jälkeen aina tarkistetaan kilpailu_ohi-metodin avulla, onko kilpailu ohi.
# Ajantasainen tilanne tulostetaan tulosta tilanne-metodin avulla kymmenen tunnin välein sekä kertaalleen sen jälkeen,
# kun kilpailu on päättynyt.


import random
import time


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

class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = []
        self.monta_autoa = autot
        i = 0
        while self.monta_autoa > 0:
            i += 1
            #tehdään auto jonka rekisteri on ABC-i ja huippunopeus on satunnainen luku väliltä 100 ja 200kmh
            self.autot.append(Auto(f"ABC-{i}", random.randint(100, 200)))
            self.monta_autoa -= 1
    def tunti_kuluu(self):
        for i in self.autot:
            self.kilpailu_ohi()
            i.kiihdytys(random.randint(-10, 15))
            i.kulje(1)
    #järjestää listan sen mukaan kuka on kulkenut pisimmän matkan, sitten tulostaa listan tilanteen
    def tulosta_tilanne(self):
        self.autot.sort(key=lambda x: x.trippi_mit, reverse=True)
        for i in self.autot:
            print(f"{i.rekkari:<10} -- {f'{i.nyky_kmh}kmh'} -- {f'{i.trippi_mit}km':>10}")
        print()
    #katsoo, onko mikään autoista mennyt yli 8000 km
    def kilpailu_ohi(self):
        testi = False
        for i in self.autot:
            if i.trippi_mit >= self.pituus:
                testi = True
                break
            else:
                testi = False
        return testi


#pää ohjelma
romuralli = Kilpailu("Suuri romuralli", 8000, 10)

while not romuralli.kilpailu_ohi():
    #time.sleep(0.75)
    romuralli.tunti_kuluu()
    romuralli.tulosta_tilanne()

print("Voittaja:")
print(f"| {romuralli.autot[0].rekkari:<7} | Nopeus: {f'{romuralli.autot[0].nyky_kmh}kmh'} | {f'Huippunopeus: {romuralli.autot[0].huippu_kmh} km':>10}")
print("__________________________________________")
romuralli.autot.pop(0)
sija = 1
for i in romuralli.autot:
    sija +=1
    print(f"| {f'Sija {sija}':<7} : {i.rekkari:<7} | {f'Nopeus: {int(i.nyky_kmh)}kmh':<15} | {f'Huippunopeus: {int(i.huippu_kmh)}kmh':20} |")