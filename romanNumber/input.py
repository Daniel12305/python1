from Funktion2zusammengefasst import romanNumber

while True:
    try: input = raw_input
    except NameError: pass
    #print("Hi " + input("Say something: "))
    gewuenschteZahl = int(input("Arabische Zahl eingeben "))
    print("Römische Zahl: " + romanNumber(gewuenschteZahl))