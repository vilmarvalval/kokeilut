#Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI)
# ja tulostaa kyseisessä maassa olevien lentokenttien lukumäärät tyypeittäin.
# Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä,
# että pieniä lentokenttiä on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne.

import mysql.connector

asemat=[]

def hae_maakoodi(koodi):
    sql = f"""SELECT
              SUM(IF(type='closed',1,0)),
              SUM(IF(type='heliport',1,0)),
              SUM(IF(type='small_airport',1,0)),
              SUM(IF(type='medium_airport',1,0)),
              SUM(IF(type='large_airport',1,0))
              FROM airport WHERE iso_country ='{koodi}';"""
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0:
        for i in tulos[0]:
            asemat.append(i)
    return tulos

#pääohjelma
yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='ville',
        password='password',
        autocommit=True
        )

print("Anna maakoodi:")
maakoodi= input().upper()
hae_maakoodi(maakoodi)
print(f"Maassa {maakoodi} on {asemat[0]} suljettuja, {asemat[1]} helikopterikenttiä, {asemat[2]} pieniä lentokenttiä, {asemat[3]} keskikokoisia lentikenttiä ja {asemat[4]} suuria lentokenttiä")