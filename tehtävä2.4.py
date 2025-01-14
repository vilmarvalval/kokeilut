luku1, luku2, luku3 = input("Anna 3 lukua siten, että niiden jokaisen välissä on vähintään 1 välilyönti: ").split()
luku1 = int(luku1)
luku2 = int(luku2)
luku3 = int(luku3)

summa=luku1+luku2+luku3
tulo=luku1*luku2*luku3
keskiarvo=(luku1+luku2+luku3)/3

print("Lukujen summa on "+str(summa)+", tulo "+str(tulo)+", keskiarvo "+str(keskiarvo))
