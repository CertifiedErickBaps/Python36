# Autor:
#          A01379896 Erick Bautista Pérez

# T=IC**n
def poblacion_total(I, C, n):
    T = I * C ** n
    return T
    
def main(): 
    I = int(input("Poblacion inicial: "))
    C = int(input("Numero de descendientes por progenitor: "))
    n = int(input("Numero de generacion: "))
    T = poblacion_total(I, C, n)    
    print("La poblacion total es", T)
    
    
main()