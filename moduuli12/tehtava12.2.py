#Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen
# ja tulostaa sitä vastaavan säätilan tekstin sekä lämpötilan Celsius-asteina.
#Perehdy rajapinnan dokumentaatioon riittävästi.
#Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi

import json
import requests
from geopy import Nominatim

geolocator = Nominatim(user_agent="get weather")
key = "33bc665ad0ed8eaed3e110ac41688d54"

#main
paikka = input("Give the name of a city: ".capitalize())

try:
    while True:
        location = geolocator.geocode(paikka)

        #katsoo jos kaupunkia ei ole olemassa
        if location is None:
            print("Invalid city name.")
            paikka = input("Give the name of a city: ".capitalize())

        #hakee kaupungin
        else:
            haku = f"https://api.openweathermap.org/data/2.5/weather?lat={location.latitude}&lon={location.longitude}&exclude={'alerts'}&appid={key}"
            try:
                tulos = requests.get(haku)
                if tulos.status_code == 200:
                    tulos = requests.get(haku).json()
                    # tulostaa sään
                    print(f"{tulos['weather'][0]['main']}: {tulos['weather'][0]['description']}")

                    # lämpötilat
                    temp = tulos['main']['temp']
                    feels = tulos['main']['feels_like']
                    # muutetaan Kelvin asteet Celsiuksiksi ottamalla absoluuttisen nollan, eli -273.15:n siitä.
                    print(f"Current temperature: {float(temp) - 273.15:.1f}°C")
                    print(f"Feels like: {float(feels) - 273.15:.1f}°C")
                    break
            except requests.exceptions.RequestException as e:
                print("Request Error:")
                print(e)
except ValueError as err:
    print("Getting geodata failed:")
    print(err)