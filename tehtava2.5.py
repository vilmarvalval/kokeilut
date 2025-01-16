leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

#muunnetaan grammoiksi, 1 leviksa vastaa 20 naulaa, 1 naula 32 luotia ja 1 luoti 13.3 grammaa.
leiviskatG = float(leiviskat*20*32*13.3)
naulatG = float(naulat*32*13.3)
luoditG = float(luodit*13.3)

kilot = int(((leiviskatG+naulatG+luoditG)/1000))
grammat = float(leiviskatG+naulatG+luoditG-(kilot*1000))

print("Massa käyttäen metristä järjestelmää on: "+str(kilot)+f"kg, ja {grammat:.2f}g.")