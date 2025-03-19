#Tehdään Auto luokka jolle annetaan mahdolliset ominaisuudet ovat huippunopeus, nykynopeus, kuljettu matka ja rekkari.
class Auto:
    huippu_kmh = 0
    nyky_kmh = 0
    trippi_mit = 0
    def __init__(self, rekkari):
        self.rekkari = rekkari
    #Tämä funktio tulostaa kaikki auton ominaisuudet ja niiden nykyiset arvot.
    def ominaisuudet(self):
        print(f"Rekkari: {self.rekkari}\n"
              f"Huippunopeus: {self.huippu_kmh}\n"
              f"Nykynopeus: {self.nyky_kmh}\n"
              f"Kuljettu matka: {self.trippi_mit}")
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
    def liiku(self, aika):
        self.trippi_mit += float(aika)*self.nyky_kmh

#luodaan auto rekisterillä "ABC-123" ja huippunopeudella 142 kmh.
auto = Auto("ABC-123")
auto.huippu_kmh = 142

while True:
    komento = input("Anna komento('kiihdytä', 'kulje' tai 'lopeta'): ")
    #kiihdyttää halutun määrän
    if komento.lower() == "kiihdytä":
        muutos = input("Anna kiihdytys määrä kilometreinä: ")
        auto.kiihdytys(muutos)
        print(f"Auton nykyinen nopeus: {auto.nyky_kmh} kmh")
    #kulkee matkan käyttäen annettua tunti määrää
    if komento.lower() == "kulje":
        kulje = input("Anna aika tunteina: ")
        auto.liiku(kulje)
        print(f"Kuljettu matka: {auto.trippi_mit} km")
    #lopettaa ohjelman käyttäjän halutessa
    if komento.lower() == "lopeta":
        auto.ominaisuudet()
        print()
        print("Hei hei!")
        break