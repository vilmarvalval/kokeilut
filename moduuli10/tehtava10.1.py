import moduulinLuokat

h = moduulinLuokat.Hissi(10,-1)
print(f"Tervetuloa hissiin. Kerroksia on {h.ylin_kerros}, alin kerros {h.alin_kerros}")

while True:
    valinta = input("Anna kerros tai paina 'enter' poistuaksesi hissistä: ")
    #lopeta ohjelma
    if valinta == "":
        break
    #jos valinta ei ole positiivinen tai negatiivinen numero
    elif not valinta.lstrip('-').isdigit():
        print("Väärä syöte.")
    #siirry kerrokseen
    else:
        h.siirry(int(valinta))