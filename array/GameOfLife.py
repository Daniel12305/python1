

generation1 = [["t", "t", "t"], ["t", "l", "l"], ["l", "t", "l"]]
nextGeneration = []

for i in range(0, 3):
    zeile = []
    for j in range(0, 3):
        zeile.append("t")
    nextGeneration.append(zeile)



zaehler = 0
for i in range(0, 3):
    for j in range(0, 3):
        if generation1[i][j] == "l":
            zaehler = zaehler + 1
           
if generation1[1][1] == "l":
    zaehler = zaehler -1
print("Zaehlerstand :" ,  zaehler)   

if zaehler == 3:
    nextGeneration[1][1] = "l"
print("ende")
#if generation1[1][1] == "t":
#    print("tote Zelle")
#    if l == 3 in generation1:
#        print("wird neugeboren")
#        generation2 = [["t", "t", "t"], ["t", "l" ,"t"], ["l", "l" ,"l"]]
#        
#    else:
#        print("wird nicht neu geboren")
#        
#if generation1[1][1] == "l":
#    print("lebende Zelle")
#    if ("l" > 3) in generation1:
#        generation2 = [["t", "t", "t"], ["t", "t" ,"t"], ["t", "t" ,"t"]]
#        print("Zellen sterben wegen Überbevölkerung")