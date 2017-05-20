# Juego de ahorcado

from random import choice
from os.path import exists

palabras = ['elefante', 'jirafa', 'hipopotamo', 
            'leon', 'tigre', 'you are ma bitch']
ahorcado = [
'''
------
|   |
|  (")
| --|--
| _/ \_
|
=========
''',
'''
------
|   |
|  (")
| --|--
| _/
|
=========
''',
'''
------
|   |
|  (")
| --|--
|
|
=========
''',
'''
------
|   |
|  (")
| --|
|
|
=========
''',
'''
------
|   |
|  (")
|   |
|
|
=========
''',
'''
------
|   |
|  (")
|
|
|
=========
''',
'''
------
|   |
|
|
|
|
=========
'''
] 
def ler_palabras():
    global palabras
    if exists('palabras.txt'):
        palabras = []
        with open('palabras.txt') as archivo:
            for p in archivo:
                palabras.append(p.rstrip()) #Borra todos los saltos de linea de la derecha
    else: 
        with open('palabras.txt', 'w') as archivo:
            for p in palabras:
                archivo.write(p + '\n')
def oculta(frase):
    r = ''
    for c in frase:
        if c.isalpha():
            r += '_'
        else:
            r += c
    return r
    
def muestra(letra, secreto, conocido):
    r = ''
    for i in range(len(secreto)):
        if letra == conocido[i]:
            r += letra
        else:
            r += secreto[i]
    return r

def escoje_palabra():
    return choice(palabras)
    
def imprime_bonito(frase):
    print(' '.join(list(frase)))
    
def lee_letra(usadas):
    while True: #Genera un ciclo infinito/controlar el punto de controlacion    
        c = input('Dame una letra: ')
        if len(c) != 1:
            print('Solo se debe teclear una letra')
        elif  not c.isalpha():
            print('Debes teclear solo una letra')
        elif c in usadas:
            print('Esta letra ya la usaste')
        else:
            return c
            
    
def juega():
    p = escoje_palabra()
    s = oculta(p)
    imprime_bonito(s)
    print()
    intentos = 6
    usadas = []
    while not(intentos == 0 or s == p):
        print('Numero de intentos: ', intentos)        
        print('Letras usadas: ', end = '') #El end sirve para juntar la linea de imprime bonito con letras usadas
        imprime_bonito(usadas)
        c = lee_letra(usadas)
        usadas.append(c)
        print()
        
        n = muestra(c, s, p)
        if n == s:
            intentos -= 1
        s = n
        imprime_bonito(s)
        print()
        
    if intentos > 0:        
        print('Felicidades eres un pinshi gay')
    else:
        print('Perdiste')
        print('La palabra secreta era: ', p)
def imprime_menu():
    print('M E N U')
    print('============')
    print('1) Jugar')
    print('2) Ver palabras')
    print('3) Salir')
    print()

def ver_palabras():
    print('-----Palabras-----')
    for p in palabras:
        print(p)
    print()
    op = input('Deseas añadir una nueva palabra? (s/n) ').upper()
    if op == 'S':
        palabra = input('Ingresa la nueva palabra: ')
        palabras.append(palabra)
        print()
        with open('palabras.txt', 'w') as archivo:
            for p in palabras:
                archivo.write(p+ '\n')
def main():
    ler_palabras()
    while True:    
        imprime_menu()
        op = input('Selecciona una opcion: ')
        if op == '1':
            juega()
        elif op == '2':
            ver_palabras()
            print()
        elif op == '3':
            print('Bye!')            
            return 
        else:
            print('Opcion incorrecta.')
main()