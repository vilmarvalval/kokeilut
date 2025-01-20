luvut=[]
print("Anna luku tai lopeta painamalla enter:")
luku=input()
while luku !="":
    luvut.append(float(luku))
    print("Anna seuraava luku tai lopeta painamalla enter:")
    luku=input()

luvut.sort(reverse=True)
print(f"Antamistasi luvuista viisi suurinta ovat {luvut[0]}, {luvut[1]}, {luvut[2]}, {luvut[3]} ja {luvut[4]}.")