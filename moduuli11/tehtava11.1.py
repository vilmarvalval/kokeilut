class Julkaisu:
    julkaisuja = 0
    def __init__(self, nimi):
        self.nimi = nimi
        Julkaisu.julkaisuja += 1
        self.numero = Julkaisu.julkaisuja
    def tulosta_tiedot(self):
        print(f'{self.numero} : {self.nimi}')

class Kirja(Julkaisu):
    def __init__(self, nimi, sivut, kirjoittaja):
        super().__init__(nimi)
        self.sivut = sivut
        self.kirjoittaja = kirjoittaja
    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f'Kirjan kirjoittaja {self.kirjoittaja}, sivumäärä {self.sivut}')

class Lehti(Julkaisu):
    def __init__(self, nimi, toimittaja):
        super().__init__(nimi)
        self.toimittaja = toimittaja
    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f'Lehden toimittaja on {self.toimittaja}')

julkaisut = []
julkaisut.append(Lehti("Aku Ankka", "Aki Hyyppä"))
julkaisut.append(Kirja("Hytti n:o 6","200","Rosa Liksom"))

for i in julkaisut:
    i.tulosta_tiedot()
    print()