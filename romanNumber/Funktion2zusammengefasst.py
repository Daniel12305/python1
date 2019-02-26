def romanNumber(zahl):
    result = ""
    
    while zahl >= 1000:
        return "M" + romanNumber(zahl - 1000)
    
    if zahl >= 900:
        return "CM" + romanNumber(zahl - 900)
    
    if zahl >= 500:
        return "D" + romanNumber(zahl - 500)
    
    if zahl >= 400:
        return "CD" + romanNumber(zahl - 400)
    
    while zahl >= 100:
        return "C" + romanNumber(zahl - 100)
    
    if zahl >= 90:
        return "XC" + romanNumber(zahl - 90)
    
    if zahl >= 50:
        return "L" + romanNumber(zahl - 50)
    
    if zahl >= 40:
        return "XL" + romanNumber(zahl - 40)
    
    while zahl >= 10:
        return "X" + romanNumber(zahl - 10)
    
    if zahl >= 9:
        return "IX" + romanNumber(zahl - 9)
    
    if zahl >= 5:
        return "V" + romanNumber(zahl - 5)
    
    if zahl >= 4:
        return "IV" + romanNumber(zahl - 4)
    
    while zahl > 0:
        return "I" + romanNumber(zahl - 1)
    
    return result
    
    