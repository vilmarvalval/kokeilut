import time
#hissin 'hitaus'(kuinka paljon odottaa kerrosten välissä)
kerros_aika = 0.5

#Hissi tehtävästä 10.1
#Tehdään hissi jolla on määritetyt ylin ja alin kerros
class Hissi:
    def __init__(self, ylin, alin):
        self.ylin_kerros = ylin
        self.alin_kerros = alin
        self.nykyinen = alin
    #siirtää hissin kerroksen ylöspäin
    def nouse(self):
        time.sleep(kerros_aika)
        self.nykyinen += 1
    #siirtää hissin kerroksen alaspäin
    def laske(self):
        time.sleep(kerros_aika)
        self.nykyinen -= 1

    #siirtää hissiä yllä olevia funktioita käyttäen
    def siirry(self,kerros):
        if self.alin_kerros <= kerros <= self.ylin_kerros:
            print("Siirrytään kerrokseen..")
        #jos kerros on suurempi tai pienempi kuin hissin ylin tai alin kerros.
        else:
            print("Kerrosta ei ole olemassa!")
            #jos kerros on suurempi kuin hissin ylin kerros, hissi asettaa ylimmän mahdollisen valituksi.
            if kerros > self.ylin_kerros:
                kerros = self.ylin_kerros
                print("Siirrytään ylimpään kerrokseen...")
            #jos kerros ei ole suurempi kuin maksimi, sen täytyy olla pienempi kuin minimi.
            #Tekee saman kuin ylempi mutta vai pienimmällä kerroksella
            else:
                kerros = self.alin_kerros
                print("Siirrytään alimpaan kerrokseen...")
        #katsoo kumpaa funktiota kutsua. Sitten kutsuu sitä while loopilla niin monta kertaa kun on tarve.
        if kerros < self.nykyinen:
            while kerros < self.nykyinen:
                self.laske()
                print(f"Nykyinen kerros {self.nykyinen}")
        if kerros > self.nykyinen:
            while self.nykyinen < kerros:
                self.nouse()
                print(f"Nykyinen kerros {self.nykyinen}")


#Talo luokka tehtävästä 10.2
class Talo:
    def __init__(self, ylin, alin, hissit):
        self.ylin = ylin
        self.alin = alin
        hissit = float(hissit)
        self.hissilista = []
        while hissit > 0:
            self.hissi = self.hissilista.append(Hissi(ylin, alin))
            hissit -= 1

    def ajah_hissi(self, valittu, kerros):
        self.hissilista[int(valittu)-1].siirry(int(kerros))

    def tulipalo(self):
        print("palohälytys!")
        for i in self.hissilista:
            i.siirry(i.alin_kerros)