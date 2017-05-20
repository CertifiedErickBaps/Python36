# x es divisible entre y? es decir de forma exacta (da 0)


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
    if m in (1, 3, 5, 7, 8, 10, 12):
     return 31
    elif m == 2:
        if leap(y):
            return 29
        else:
            return 28
    else:
        return 30
        
def next_day(y, m, d):
    if m == 12 and d == num_dias_mes(m, y):
        return y + 1, 1, 1 # se regresa al primero de enero del año siguiente
    elif d == num_dias_mes(m, y):
        return y, m + 1, 1
    else: 
        return y, m, d + 1
     
def main():
    print(leap(2015))
    print(leap(2016))
    print(leap(2000))
    print(leap(2100))
    print(next_day(2015, 2, 13))
    print(next_day(2015, 2, 28))
    print(next_day(2016, 2, 28))
    print(next_day(2016, 12, 31))

        
main()        
        
# Los caminos deben de llegar a un resultado cada if tiene que venir con un else
        