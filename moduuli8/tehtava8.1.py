#Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin.
# Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen ja
# sen sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta.
# ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen.

import mysql.connector

def hae_lentoasema(koodi):
    sql = f"SELECT name FROM airport WHERE ident = '{koodi}';"
    #print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    #print(tulos)
    if kursori.rowcount >0:
        return tulos[0]

#pääohjelma
yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='ville',
        password='password',
        autocommit=True
        )



print("Anna lentokentän ICAO-koodi:")
asemakoodi= input().upper()
print(f"{asemakoodi} on {hae_lentoasema(asemakoodi)[0]}")
