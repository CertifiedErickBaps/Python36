#@author: Erick Bautista Perez A01379896

def polinomio(x, coefs):
    #a = (coefs[::-1])
    
    b = 0
    lista = []
    for i in coefs:
        if not i == 0:
           b += 1
           lista.append(b)
           
    lista.reverse()
    print(lista)
    resultado = 0    
    for i in lista:
        
        print(lista)
        for c in coefs:
            multiplicacion = x * (c ** i)
            print()
        
def main():
    print(polinomio(3.14, [1]))
    print(polinomio(3.0, [4, 3, -3]))
    print(polinomio(2.5, [-2, 3, -1, 0, 5]))
    print(polinomio(-1.0, [1, 1, 1, 1, 1, 1]))
main()