#tehdään Auto luokka jolle annetaan mahdolliset ominaisuudet ovat huippunopeus, nykynopeus, kuljettu matka ja rekkari.
class Auto:
    huippu_kmh = 0
    nyky_kmh = 0
    trippi_mit = 0
    def __init__(self, rekkari):
        self.rekkari = rekkari
    #funktio jonka avulla auto saadaan kiihdyttämään.
    # Kiihdytyksen jälkeen funktio katsoo, onko nopeus mennyt yli auton huippunopeuden tai alle nollan.
    # Jos on, niin se korjaa nopeuden maksimiin tai negatiivisen tapauksessa nollaan.
    def kiihdytys(self, nopeusmuutos):
        self.nyky_kmh += nopeusmuutos
        if self.nyky_kmh > self.huippu_kmh:
            self.nyky_kmh = self.huippu_kmh
        if self.nyky_kmh < 0:
            self.nyky_kmh = 0
    #Tämä funktio tulostaa kaikki auton ominaisuudet ja niiden nykyiset arvot.
    def ominaisuudet(self):
        print(f"Rekkari: {self.rekkari}\n"
              f"Huippunopeus: {self.huippu_kmh}\n"
              f"Nykynopeus: {self.nyky_kmh}\n"
              f"Kuljettu matka: {self.trippi_mit}")

#luodaan auto rekisterillä "ABC-123" ja huippunopeudella 142 kmh.
auto = Auto("ABC-123")
auto.huippu_kmh = 142

#kiihdytys testit
auto.kiihdytys(30)
print(auto.nyky_kmh)
auto.kiihdytys(70)
print(auto.nyky_kmh)
auto.kiihdytys(50)
print(auto.nyky_kmh)
auto.kiihdytys(-200)
print(auto.nyky_kmh)