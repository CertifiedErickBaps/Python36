# Autores: 
#          A01379896 Erick Bautisa Perez
#          A01378568 Leonardo Valencia Benitez
#
# Desarrollar en Python 3.5 una aplicación que implemente el juego de Rompe Códigos, 
#que es una variación del juego comercial conocido como “Mastermind” de Pressman Toys.
#
# Noviembre 30, 2016.
from random import choice, shuffle
from os.path import exists
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
'n', 'o', 'p', 'q', 'r', 's','t', 'u', 'v', 'w', 'x', 'y', 'z']
def interfaz():
    print('**ROMPE CODIGOS**')
    print('       Menú')
    print('===================')  
    print('1. Jugar','\n2. Configuración','\n3. Salir', )
    print('===================')

def configuracion():
    a = 4
    b = 6
    c = 10
    while not exists("configuracion.txt"):
        with open("configuracion.txt", "w") as archivo:
            archivo.write(str(a) + "\n"+ str(b) + "\n" + str(c) + "\n" )
        
    if exists ("configuracion.txt"):
        with open("configuracion.txt", "r") as archivo:
            a = int(archivo.readline())            
            b = int(archivo.readline())            
            c = int(archivo.readline())            
        print ("----- Configuración -----")
        print ("Longitud del codigo a romper: " , a)
        print("Letras distintas posibles: ", b)
        print("Máximo número de intentos: ", c)
        x = input("¿Deseas modificar estos valores? (s/n): ").upper()
        if x == "S":
            w = input("Longitud del codigo a romper: ")
            while not w.isdigit() or int(w) < 2 or int(w)>26:
                print(w, " no es un número entero positivo válido.")
                w = input("Longitud del codigo a romper: ")
            y = input("Letras distintas posibles: ")
            while not y.isdigit() or int(y) < int(w) or int(y) > 26:
                print ("El número debe estar entre", w, "y 26.")
                y = input("Letras distintas posibles: ")
            z = input("Máximo número de intentos: ")
            while z.isalpha() or int(z) <1 or int(z) >99:
                print(z, "no es un número entero positivo válido.")
                z = input("Máximo número de intentos: ")
            a = w
            b = y
            c = z
            print()
            with open("configuracion.txt", "w") as f:
                f.write( a + "\n" + b + "\n" + c + "\n" )
            print("Los cambios han sido guardados exitosamente")
        
def jugar():
    while not exists("configuracion.txt"):   
        with open("configuracion.txt", "w") as archivo:
            archivo.write(str(4) + "\n"+ str(6) + "\n" + str(10) + "\n" )
    else:
        with open("configuracion.txt", "r") as archivo:
            a = int(archivo.readline())            
            b = int(archivo.readline())            
            c = int(archivo.readline())            

    codigo = ''
    cant_digitos = a
    particion = b
    intentos = c

    particion_letras = letras[:particion]
    shuffle(particion_letras)
    #print(particion_letras)
#==============================================================================
    for c in range(cant_digitos):
        elegido = choice(particion_letras)
        while elegido in codigo:        
            elegido = choice(particion_letras)            
        codigo += elegido
    #print(codigo)
#==============================================================================
    intentos2 = 0    
    while intentos != 0:
        aciertos = 0
        errores = 0 
        
        print('Intentos restantes para romper el codigo: ', intentos)
        print()
        print('Teclea una cadena de', cant_digitos, 'caracteres', 'de la A a la', 
              letras[particion - 1].upper(), ': ' ,end = '')
        propuesta = input().lower()
        
        if repetidos(list(propuesta)): 
            print ("La cadena no debe tener caracteres repetidos")
            
        elif len(propuesta) == len(codigo):
            intentos -= 1
            intentos2 += 1
            for i in range(cant_digitos):
                if propuesta[i] == codigo[i]:
                    aciertos += 1
                else:
                    errores += 1        
            print('Letras en posicion correcta: ', aciertos, '\nLetras en posicion incorrecta: ', errores)            
            print()
            
            if propuesta == codigo:        
                print('Felicidades! \nRompiste el codigo en', intentos2, 'intentos')
                break
        else:
            print('La cadena debe ser de exactamente', cant_digitos ,'caracteres.')   
    if intentos == 0:    
        print('Ya llegaste al numero maximo de intentos.\nEl codigo era: ', codigo.upper())

def repetidos(n):
    new_list = list(set(n))
 
    if len(new_list) != len(n):
        return True #Retorna True si hay duplicados       #Referencia y ayuda de Juan Fierro en esta definicion
    else:
        return False #Retorna False si no hay duplicados
                  
def main():
    while True:
        interfaz()
        opcion = input('Selecciona una opcion: ')
        if opcion == '1':
            jugar()
            print()
        elif opcion == '2':
            configuracion()
            print()
        elif opcion == '3':
            print('Bye!')
            return
        else:
            print()            
            print('Opcion invalida.')  
            print()
    
main()    