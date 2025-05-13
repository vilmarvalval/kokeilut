#Toteuta taustapalvelu, joka palauttaa annettua lentokentän ICAO-koodia vastaavan lentokentän nimen
# ja kaupungin JSON-muodossa. Tiedot haetaan opintojaksolla käytetystä lentokenttätietokannasta.
#Esimerkiksi EFHK-koodia vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/kenttä/EFHK.
#Vastauksen on oltava muodossa: {"ICAO":"EFHK", "Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}.

import mysql.connector
from flask import Flask

app = Flask(__name__)

yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='ville',
        password='password',
        autocommit=True
        )

@app.route('/kenttä/<airport>')
def find_airport(airport):
    cursor = yhteys.cursor()
    cursor.execute(f"SELECT name FROM airport WHERE ident = '{airport}';")
    airport_name = cursor.fetchall()
    cursor.execute(f"SELECT municipality FROM airport WHERE ident = '{airport}';")
    airport_municipality = cursor.fetchall()

    #tämä jättää ekstra hakasulkeet vastaukseen mutta sillä ei kai ole mitään väliä.
    #En keksinyt miten listan saisi oikeaan järjestykseen muuten.
    return [
        {'ICAO': airport},
        {'Name': airport_name[0][0]},
        {'Municipality': airport_municipality[0][0]}
    ]

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)


#{"ICAO":"EFHK","Municipality":"Helsinki","Name":"Helsinki Vantaa Airport"}
#{"ICAO":"EFHK", "Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}
#[{"ICAO":"EFHK"},{"Name":"Helsinki Vantaa Airport"},{"Municipality":"Helsinki"}]