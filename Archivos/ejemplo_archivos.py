#Formas de leer un archivo
def prueba1():
    with open('prueba.txt') as f:
        s = f.read() #Leer un archivo completo
    print(s)

def prueba2():
    with open('prueba.txt') as f:
        s = 'x'
        while s != '': #Para que no sea la cadena vacia
                s = f.readline() #Ir leyendo una linea a la vez
                
                if s != '':
                    print(s[:-1]) #Para que no nos de doble salto de linea, hay que agregarle el nuevo valor con end y una cadena vacia
def prueba3():
    with open('prueba.txt') as f:
        r = f.readlines()
    for linea in r:
        print(linea, end = '')
def prueba4():
    with open('prueba.txt') as f:
        for linea in f:
            print(linea, end= '')
            
def prueba5():
    with open('dieces.txt', 'w') as f:
        for i in range(10, 1001, 10):
            f.write(str(i) + '\n') #Tienes que dar un valor y un salto de linea
            
def prueba6():
    with open('uno.txt') as f1, open('dos.txt') as f2, open('tres.txt', 'w') as f3:
        contenido1 = f1.read()
        contenido2 = f2.read()
        f3.write(contenido1)
        f3.write(contenido2) #Solo recibe un solo valor y para unirlos se anida a dos
        
        

def main():
    #prueba1()#Te da el valor en un solo golpe
    #prueba2()#Lee la primera linea    
    #prueba3()
    #prueba4()
    prueba5()
main()

