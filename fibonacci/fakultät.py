def fakultät(zahl):
    if zahl > 1:
        return zahl * fakultät(zahl - 1)
    else:
        return 1
    

