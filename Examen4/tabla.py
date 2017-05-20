#Erick Bautista Perez A01379896

def tabla(n, archivo_salida):
    with open(archivo_salida, 'w') as f:
        r = 0        
        for i in range(1, 11):
            r = n * i
            f.write(str(n) + ' x ' + str(i) + ' = ' + str(r) + '\n')
    
def main():
    tabla(2, 'tabla2.txt')
    tabla(7, 'tabla7.txt')
main()

