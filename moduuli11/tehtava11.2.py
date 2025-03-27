import random

class Auto:
    id = 0
    def __init__(self, rekkari, huippu_kmh, kantama_km):
        self.rekkari = rekkari
        self.huippu_kmh = huippu_kmh
        self.kantama_km = kantama_km
        self.nyky_kmh = 0
        self.trippi_km = 0
        self.ajo_h = 0
        Auto.id += 1
        self.id = Auto.id

    #tulostaa ajoneuvon yleiset tiedot
    def tulosta_tiedot(self):
        print(f'Auto {self.id}: {self.rekkari}\n'
              f'trippi mittari {self.trippi_km}km\n'
              f'ajotunnit: {self.ajo_h}')

    #ajaa annetun tuntimäärän
    def aja(self, tunnit):
        self.trippi_km += self.nyky_kmh
        self.ajo_h += tunnit




class EAuto(Auto):
    def __init__(self, rekkari, huippu_kmh, kantama, akku_kwh):
        super().__init__(rekkari, huippu_kmh, kantama)
        self.akku_koko = akku_kwh
        self.akku_lataus = akku_kwh

    #lataa auton akun
    def lataa(self):
        print(f'Ladataan {self.rekkari}:n akkua.')
        self.akku_lataus = self.akku_koko

    #kuluttaa akkua auton nopeuden, kantaman ja ajon ajan mukaan ja reagoi jos akku on tyhjä
    def aja(self, tunnit):
        super().aja(tunnit)
        self.akku_lataus -= self.akku_koko * ((self.nyky_kmh * tunnit) / self.kantama_km)
        if self.akku_lataus <= 0:
            print(f'{self.rekkari}:n akku on tyhjä!')
            self.lataa()


    #tulostaa sähköautolle uniikit tiedot
    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f'Akun lataus: {self.akku_lataus:.2f}/{self.akku_koko} kWh.')


class PAuto(Auto):
    def __init__(self, rekkari, huippu_kmh, kantama, tankki_koko):
        super().__init__(rekkari, huippu_kmh, kantama)
        self.tankki_koko = tankki_koko
        self.tankki_bensa = tankki_koko

    #tankkaa auton
    def tankkaa(self):
        print(f'Tankataan {self.rekkari}:n tankkia.')
        self.tankki_bensa = self.tankki_koko

    #kuluttaa polttoainetta auton nopeuden, kantaman ja ajon ajan mukaan ja reagoi jos tankki on tyhjä
    def aja(self, tunnit):
        super().aja(tunnit)
        self.tankki_bensa -= self.tankki_koko * ((self.nyky_kmh * tunnit) / self.kantama_km)
        if self.tankki_bensa <= 0:
            print(f'{self.rekkari}:n tankki on tyhjä!')
            self.tankkaa()

    #tulostaa polttomoottoriautolle uniikit tiedot
    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f'Bensan määrä: {self.tankki_bensa:.2f}/{self.tankki_koko} litraa.')

autot = [
    EAuto("ABC-15", 180, 1000, 52.5),
    PAuto("ACD-123", 165, 1000, 32.3)
    ]

for i in autot:
    i.nyky_kmh = random.randint(100, i.huippu_kmh)
tunti = 0
while tunti < 3:
    for i in autot:
        i.aja(1)
    tunti += 1

for i in autot:
    i.tulosta_tiedot()
    print()