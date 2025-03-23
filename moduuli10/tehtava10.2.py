#Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä. Hissien lista tallennetaan talon ominaisuutena.
#Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin numeron ja kohdekerroksen.
#Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.
import moduulinLuokat
hissiluku = 3
talo = moduulinLuokat.Talo(15, -1, hissiluku)

print(f"Tervetuloa taloon. Hissejä on {len(talo.hissilista)}.")
while True:
    valinta = input("Anna hissin numero tai paina 'enter' poistuaksesi hissistä: ")
    if valinta == "":
        break
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
                talo.ajah_hissi(talo.hissilista[int(valinta)-1],kerros)
    else:
        print(f"Talossa on {hissiluku} hissiä! Ei {valinta}!")