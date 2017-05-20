def sumatoria_consecutiva(n):
    s = 0 #s es un acumulador
    for x in range(1, n+1):
        s = s + x
    return s#Inicio del ciclo

def sumatoria_de_gauss(n):
    return int((n/2)*(n+1))
    
def factorial(n):
    y = 1
    for z in range(1, n+1):
        y = y*z # o r*=i
    return y#Termina y regresa

def main():
    n = 5
    r1 = sumatoria_consecutiva(n)
    r2 = sumatoria_de_gauss(n)
    r3 = factorial(n)
    print(r1)
    print(r2)
    print(r3)
main()