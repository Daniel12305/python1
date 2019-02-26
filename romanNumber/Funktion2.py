def romanNumber(zahl):
    result = ""
    zwischenwert = zahl

    while (zwischenwert / 1000)>= 1:
        result = result + "M"
        zwischenwert = zwischenwert - 1000

    if (zwischenwert / 900)>= 1:
        result = result + "CM"
        zwischenwert = zwischenwert - 900

    if (zwischenwert / 500)>= 1:
        result = result + "D"
        zwischenwert = zwischenwert - 500
 
    if (zwischenwert / 400)>= 1:
        result = result + "CD"
        zwischenwert = zwischenwert - 400        

    while (zwischenwert / 100)>= 1:
        result = result + "C"
        zwischenwert = zwischenwert - 100
    
    if (zwischenwert / 90)>= 1:
        result = result + "XC"
        zwischenwert = zwischenwert - 90

    if (zwischenwert / 50)>= 1:
        result = result + "L"
        zwischenwert = zwischenwert - 50
        
    if (zwischenwert / 40)>= 1:
        result = result + "XL"
        zwischenwert = zwischenwert - 40        

    while (zwischenwert / 10)>= 1:
        result = result + "X"
        zwischenwert = zwischenwert - 10
    
    if (zwischenwert / 9)>= 1:
        result = result + "IX"
        zwischenwert = zwischenwert - 9
        
    if (zwischenwert / 5)>= 1:
        result = result + "V"
        zwischenwert = zwischenwert - 5

    if (zwischenwert / 4)>= 1:
        result = result + "IV"
        zwischenwert = zwischenwert - 4

    while zwischenwert > 0:
        result = result+"I"
        zwischenwert = zwischenwert -1       
            
    return result