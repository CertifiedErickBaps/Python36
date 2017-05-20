
def factorial(n):
    r = 1
    for i in range(1, n + 1):
        r *= i
      
    return r
        
def combinaciones(m,n):
    return int(factorial(m)/(factorial(n)* factorial(m-n)))

def main():
    print(combinaciones(5, 2))# imprimir siempre en el main
    
main()