import math

def virhekoppi(x):
    try:
        x = float(x)
    except:
        print("Virheeellinen syöte, annathan vain numeron.")
    return float (x)

def pitsalaskin(hinta, halkasija):
    metrihinta = (hinta / ((((halkasija / 100) / 2) ** 2) * math.pi))
    #metrihinta = hinta/((halkasija/100)**2)
    return metrihinta

halka1 = 0
hinta1 = 0

halka2 = 0
hinta2 = 0

print("Anna ensimmäisen pitsan nimi:")
nimi1 = input()
while halka1 == 0:
    print("Anna ensimmäisen pitsan halkasiaja senttimetreinä:")
    halka1 = input()
    halka1 = virhekoppi(halka1)

while hinta1 == 0:
    print("Anna ensimmäisen pitsan hinta:")
    hinta1 = input()
    hinta1 = virhekoppi(hinta1)

print("Anna vertailtavan pitsan nimi:")
nimi2 = input()
while halka2 == 0:
    print("Anna vertailtavan pitsan halkasiaja senttimetreinä:")
    halka2 = input()
    halka2 = virhekoppi(halka2)

while hinta2 == 0:
    print("Anna vertailtavan pitsan hinta:")
    hinta2 = input()
    hinta2 = virhekoppi(hinta2)

pitsa1 = pitsalaskin(hinta1,halka1)
pitsa2 = pitsalaskin(hinta2,halka2)

print(f"Pitsa 1 maksaa {pitsa1:.2f}€/m² ja pitsa 2 maksaa {pitsa2:.2f}€/m².")
if pitsa1 > pitsa2:
    print(f"{nimi2}:lla on siis alhaisempi yksikköhinta.")
elif pitsa1 < pitsa2:
    print(f"{nimi1}:lla on siis alhaisempi yksikköhinta.")
else:
    print("Pitsoilla on siis sama yksikköhinta.")