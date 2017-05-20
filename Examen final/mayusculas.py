#@author: Erick Bautista Perez A01379896


def mayusculas(archivo_entrada, archivo_salida):
    with open(archivo_entrada, 'r') as f:
        f = f.readlines()
        
    with open(archivo_salida, 'w') as f1:
        for i in f:
            if not i.isupper():
                mayusculas = (i.upper())
                f1.write(mayusculas)
            else:
                f1.write(i)
    
    
def main():
    mayusculas('entrada1.txt', 'salida1.txt')
    mayusculas('entrada2.txt', 'salida2.txt')
main()