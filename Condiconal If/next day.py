def leap(y):

    if y % 4 == 0: # % para que me de 0, si me cumple esta se va a abajo

        if y % 100 == 0: #Aqui es divisible entre 100 y por lo tanto no es biciesto

            if y % 400 == 0:
                return True

            else:
                return False
                
        else:
            return True
    else:
        return False #La primera letra en mayuscula, no es biciesto

def num_dias_mes(m, y):
    if m == 1 or m == 3 or m == 5 or m == 7\
        or m == 8 or m == 10 or m == 12:
        return 31
    elif m == 2:
        if leap(y):
            return 29
        else:
            return 28
    else:
        return 30

def next_day(y, m, d):
    print()  