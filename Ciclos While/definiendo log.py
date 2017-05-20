
def log2(n):
    c = -1  #este es el contador    
    while n != 0:
        n //= 2
        c += 1
    return c #si no le ponemos regresar dara un none, es fundamental para poder repetir el valor.
    


def main():
    print(log2(500))
    print(log2(1))
    print(log2(0))
    print(log2(1024))
    print(log2(1023))
main()