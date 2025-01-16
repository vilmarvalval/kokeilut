numero = float(input("Anna numero: "))
pienin = numero
suurin = numero
while numero!="":
    numero = input("Anna seuraava numero tai syötä tyhjä merkkijono lopettaaksesi: ")
    if numero == "":
        break
    numero = float(numero)
    if numero < pienin:
        pienin = numero
    if numero > suurin:
        suurin = numero

print(f"Pienin antamasi numero oli {pienin}, ja suurin {suurin}")