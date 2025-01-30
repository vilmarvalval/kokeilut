luvut =[]
luku = 0
def summa():
    summa = sum(luvut)
    return summa

while luku !="":
    try:
        luvut.append(int(luku))
    except:
        print("Tuo ei ole kokonaisluku.")
    else:
        luvut.append(int(luku))
    print("Anna kokonais luku tai lopeta painamalla enter:")
    luku = input()

print(f"Yhteensä {summa()}")
