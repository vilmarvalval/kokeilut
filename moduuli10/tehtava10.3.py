#Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa on parametriton metodi palohälytys,
# joka käskee kaikki hissit pohjakerrokseen. Jatka pääohjelmaa siten, että talossasi tulee palohälytys.
import moduulinLuokat

hissiluku = 3
talo = moduulinLuokat.Talo(15, -1, hissiluku)

print(f"Tervetuloa taloon. Hissejä on {len(talo.hissilista)}.")
while True:
    valinta = input("Anna hissin numero tai paina 'enter' poistuaksesi talosta: ")
    if valinta == "":
        break
    elif valinta == "hälytys":
        talo.tulipalo()
    elif not valinta.isdigit():
        print("Väärä syöte.")
    elif hissiluku >= int(valinta) > 0:
        while True:
            kerros = input("Anna kerros tai paina 'enter' poistuaksesi hissistä: ")
            if kerros == "":
                break
            # jos kerros ei ole numero
            elif not kerros.lstrip('-').isdigit():
                print("Väärä syöte.")
            else:
                print(f"Hissi numero {valinta} valittu.")
                #ajaa valittua hissiä
                talo.ajah_hissi(valinta,kerros)
    else:
        print(f"Talossa on {hissiluku} hissiä! Ei {valinta}!")