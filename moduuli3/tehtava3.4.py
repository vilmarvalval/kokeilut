vuosi =  float(input("Anna tarkistettava vuosi: "))

if vuosi % 400 == 0 or (vuosi % 100 != 0 and vuosi % 4 == 0):
    print("Vuosi on karkaus vuosi!")
else:
    print("Vuosi ei ole karkausvuosi.")

