import math

vuodenajat = ("Syksy","Kesä","Kevät","Talvi")

print("Anna kuukauden numero:")
kuukausi = input()
try: int(kuukausi)
except:
    print("Tuo ei ole kuukauden numero")
else:
    kuukausi = math.floor((11-int(kuukausi))/3)
    if kuukausi <=12:
        print(vuodenajat[kuukausi])
    else:
        print("Antamasi numero on isompi kuin kuukausien määrä.")