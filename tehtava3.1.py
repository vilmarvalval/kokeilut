pituus = float(input("Anna saamasi kuhan pituus senttimetreinä: "))
vertausPituus = 37-pituus

if pituus < 37:
    print(f"Kuha on alimittainen({vertausPituus:.2f}cm liian lyhyt.), laske se takaisin.")
else:
    print("Voit pitää kuhan.")