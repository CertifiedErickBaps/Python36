def sign(n):
    if n < 0:
        return -1
        
    elif n > 0:
        return 1
       
    else:
        return 0
       
def main():
    print(sign(-10))
    print(sign(5))
    print(sign(0))
    
main()
    #if n == 0: #asignar valores, es una comparacion, si uno es igual a otra n es igual a 0
       #return 0
       
    