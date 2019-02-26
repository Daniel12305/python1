

def ggt(zahl1, zahl2):
    while zahl1 and zahl2 != 0:
        h = zahl1 % zahl2
        zahl1 = zahl2
        zahl2 = h
    return zahl1

while True:
    zahl1 = int(input("1. Zahl? "))
    zahl2 = int(input("2. Zahl? "))
    print("Der größte gemeinsame Teiler ist:", ggt(zahl1, zahl2))