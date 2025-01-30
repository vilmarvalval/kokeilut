lista=[]
luku=1

def karsija(x):
    n = 0
    while n !=len(x):
        if (x[n]) % 2 != 0:
            x.pop(n)
        else:
            n = n+1
    return x

while luku !="":
    print("Anna kokonaisluku tai lopeta painamalla enter")
    luku = input()
    if luku =="":
        break
    try:
        lista.append(int(luku))
    except:
        print("Tuo ei ole kokonaisluku.")

#print(f"Alkuperäinen: {lista}")
#karsija()
#print(f"Parittomat karsittu: {lista}")

x= karsija(lista.copy())
print(f"Alkuperäinen: {lista}")
print(f"Parittomat karsittu: {x}")