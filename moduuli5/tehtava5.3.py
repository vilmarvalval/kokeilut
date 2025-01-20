#oma kokeilu suorituksen keston havainnollistamiseksi + pientä kommenttien käyttämis harjoittelua

print("Anna kokonaisluku: ")
kokeiltava = int(input())
prosentti = 0
print("")
if kokeiltava > 1:
        for i in range(2,(kokeiltava//2)+1):
            if round((i/kokeiltava)*200) > prosentti:
                print(str(round((i/kokeiltava)*200))+"%")
                prosentti = round((i / kokeiltava) * 200)
            if (kokeiltava % i) == 0:
                print(f"Luku {kokeiltava} ei ole alkuluku.")
                break
        else:
            print(f"Luku {kokeiltava} on alkuluku.")
else:
    print(f"Luku {kokeiltava} ei ole alkuluku.")


#Tämä tehtävä oli siitä hieman hankala että materiaalissa ei ollut mitään viittauksia siihen miten alkuluvun voi laskea.
#Esim. Pienillä lakuluvuilla on vielä sinänsä helppo kokeilla kaikki sitä edeltävät alkuluvut mutta jos tätä jatkaa,
# niin merkkimäärä lähtee nopeasti käsistä.