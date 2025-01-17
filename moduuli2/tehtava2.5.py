leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

#muunnetaan grammoiksi, 1 leviksa vastaa 20 naulaa, 1 naula 32 luotia ja 1 luoti 13.3 grammaa.
leiviskatG = leiviskat*20*32*13.3
naulatG = naulat*32*13.3
luoditG = luodit*13.3

kilot = ((leiviskatG+naulatG+luoditG)//1000)
grammat = leiviskatG+naulatG+luoditG-(kilot*1000)

print(f"Massa käyttäen metristä järjestelmää on: {kilot:.0f}kg, ja {grammat:.2f}g.")