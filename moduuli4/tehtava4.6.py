import random

print("Tämä on piin likiarvolaskuri.")
print("Mitä suuremman arvon syötät, sitä tarkempi likiarvo on.")
print("Syötä haluamasi tarkkuus arvo(arvottujen pisteiden määrä): ")
kerrat = int(input())

testaus = 0
ympyras = False
onnistuneet = 0
print("Lasketaan...")
prosentti = 0
while testaus <= kerrat:
    SatX = random.uniform(1, -1)
    SatY = random.uniform(1, -1)
    if (SatX**2)+(SatY**2) < 1:
         onnistuneet = onnistuneet+1
    testaus = testaus + 1
    prosentti = (testaus/kerrat)*100
    if prosentti % 1 == 0:
        print(f"{prosentti:.0f}%")
piinArvo = 4*onnistuneet/kerrat

print(f"Laskettu piin likiarvo on {piinArvo}")
