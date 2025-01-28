gallona = 1

def gallonoiksi():
    litrat = gallona*3.785
    return litrat

while gallona >= 0:
    print("Anna gallonamäärä:")
    gallona = input()
    try:
        gallona = float(gallona)
    except:
        print("Syöte ei ole sallittu luku, kirjoitathan vain numeron.")
        gallona = 0
    else:
        gallona = float(gallona)
        if gallona <= -1:
            break
        else:
            print(f"{gallona} gallonaa on {gallonoiksi():.2f} litraa")