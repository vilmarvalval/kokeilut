sukupuoli = input("Kerro biologinen sukupuolesi: ")
hemoArvo = float(input("Kerro hemoglobiini arvosi  g/l: "))

if sukupuoli == "nainen":
    if hemoArvo > 175:
        print("Hemoglobiiniarvosi on korkea!")
    elif hemoArvo < 175 and hemoArvo > 117 or hemoArvo == 175 or hemoArvo == 117:
        print("Hemoglobiiniarvosi on normaali.")
    elif hemoArvo < 117:
        print("Hemoglobiiniarvosi on alhainen!")

if sukupuoli == "mies":
    if hemoArvo > 195:
        print("Hemoglobiiniarvosi on korkea!")
    elif hemoArvo < 195 and hemoArvo > 134 or hemoArvo == 195 or hemoArvo == 134:
        print("Hemoglobiiniarvosi on normaali.")
    elif hemoArvo < 134:
        print("Hemoglobiiniarvosi on alhainen!")