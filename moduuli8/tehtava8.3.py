from geopy import distance
import mysql.connector

def hae_lentoasema(koodi):
        sql = f"""
                SELECT latitude_deg, longitude_deg FROM airport WHERE gps_code = '{koodi}';
        """
        kursori = yhteys.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchall()
        if kursori.rowcount > 0:
                return tulos

yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='ville',
        password='password',
        autocommit=True
        )

print("Anna ensimmäisen lentokentän ICAO-koodi:")
asemakoodi1 = input().upper()
print("Anna toisen lentokentän ICAO-koodi:")
asemakoodi2 = input().upper()

print(f'Lentokenttien välinen matka on {distance.distance(hae_lentoasema(asemakoodi1),hae_lentoasema(asemakoodi2))}')