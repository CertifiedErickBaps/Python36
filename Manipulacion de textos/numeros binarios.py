# Definiendo un numero con binarios

def binario(n):
    if n == 0:
        return "0"    
    if n < 0:
        negativo = True
    else:
        negativo = False
    n = abs(n)
    
    
    r = ""
    while n != 0:
        r = str(n % 2) + r
        n //= 2
        
    if negativo:
        r = "-" + r
    return r
    
def main():
    print(binario(12))
    print(binario(6))
    print(binario(3))
    print(binario(0))
main()
#Los numeros negativos en binario hay que agregarle en return -r