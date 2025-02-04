kuukaudet = ("joulukuu","tammikuu","helmikuu","maaliskuu","huhtikuu","toukokuu","kesäkuu","heinäkuu","elokuu","syyskuu","lokakuu","marraskuu")

print("Anna kuukausi:")
kuukausi = input().lower()

if kuukausi in kuukaudet:
    if kuukaudet.index(kuukausi) <= 2:
        print("Kuukausi on talvella.")
    elif kuukaudet.index(kuukausi) <= 5:
        print("Kuukausi on keväällä.")
    elif kuukaudet.index(kuukausi) <= 8:
        print("Kuukausi on kesällä.")
    else:
        print("Kuukausi on syksyllä.")
else:
    print(f"Kuukausi {kuukausi} ei löytynyt kuukausista.")