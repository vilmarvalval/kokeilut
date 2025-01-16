tuuma = 0
while tuuma >= 0:
    tuuma = float(input("Anna senttimetreiksi muutettavat tuumat: "))
    sentit = tuuma*2.54
    if tuuma < 0:
        break
    print(f"{sentit:.2f}cm")
