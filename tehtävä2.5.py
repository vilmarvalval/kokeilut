leviksat = float(input("Anna leviksät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

#muunnetaan grammoiksi, 1 leviksa vastaa 20 naulaa, 1 naula 32 luotia ja 1 luoti 13.3 grammaa.
leviksatG = float(leviksat*20*32*13.3)
naulatG = float(naulat*32*13.3)
luoditG = float(luodit*13.3)

kilot = int(((leviksatG+naulatG+luoditG)/1000))
grammat = int((leviksatG+naulatG+luoditG-(kilot*1000))*1000)

print("Massa käyttäen metristä järjestelmää on: "+str(kilot)+"kg, ja "+str(grammat/1000)+"g.")