    #Erick Bautista Pérez   A01379896
#Conociendo la moda
# moda
def moda(archivo_entrada):
    with open(archivo_entrada, 'r') as f:
        lista = []
        for i in f.readlines():
            lista.append(i.rstrip())
        

        repeticiones = 0
        for i in lista:
            apariciones = lista.count(i)                                                       
            if apariciones > repeticiones:                                                       
                repeticiones = apariciones                                                       
                                                                                         
        modas = [] 
        for i in lista:                                                       
            apariciones = lista.count(i)                                                             
            if apariciones == repeticiones and i not in modas:                                   
                modas.append(i)     
        modas.sort()
        return modas

def antimoda(archivo_entrada):   
    with open(archivo_entrada, 'r') as f:
        lista = []
        for i in f.readlines():
            lista.append(i.rstrip())
        

        repeticiones = 0
        for i in lista:
            apariciones = lista.count(i)                                                       
            if apariciones < repeticiones:                                                       
                repeticiones = apariciones                                                       
                                                                                         
        desmodas = [] 
        for i in lista:                                                       
            apariciones = lista.count(i)                                                             
            if apariciones != repeticiones and i not in desmodas:                                   
                desmodas.append(i)     
        desmodas.sort()
        return desmodas                                       
                                                                                         
def main():
    print(moda('prueba1.txt'))
    print(moda('prueba2.txt'))
    print(moda('prueba3.txt'))
    print(moda('prueba4.txt'))
    print(moda('prueba5.txt'))
    print(moda('prueba6.txt'))
    print()
    print(antimoda('prueba1.txt'))
    print(antimoda('prueba2.txt'))
    print(antimoda('prueba3.txt'))
    print(antimoda('prueba4.txt'))
    print(antimoda('prueba5.txt'))
    print(antimoda('prueba6.txt'))
    

main()