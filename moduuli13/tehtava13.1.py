#Toteuta Flask-taustapalvelu, joka ilmoittaa, onko parametrina saatu luku alkuluku vai ei.
#Hyödynnä toteutuksessa aiempaa tehtävää, jossa alkuluvun testaus tehtiin.
#Esimerkiksi lukua 31 vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/alkuluku/31.
#Vastauksen on oltava muodossa: {"Number":31, "isPrime":true}.
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/alkuluku/')
def annaalkuluku():
    return 'Kirjoita alkuluku URLlän perään.'

@app.route('/alkuluku/<int:luku>/')
def alkuluku(luku):
    isprime = False
    if luku > 1:
        for i in range(2, (luku // 2) + 1):
            if (luku % i) == 0:
                isprime = False
                break
            else:
                isprime = True

    return {
        'Number': luku,
        'isPrime': isprime
    }

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)