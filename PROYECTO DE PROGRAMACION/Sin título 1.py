from random import choice         


continuar = 1
while continuar == 1:
    print('Bienvenido a matermind')
    
    print('Elija dificultad de juego 1 easy, 2 hard, 3 pesadilla')
    dificultad = int(input('Digite el numero de dificultad: '))
    if dificultad == 1:
        cant_digitos = 3
    elif dificultad == 2:
        cant_digitos = 4
    elif dificultad == 3:
        cant_digitos = 5
    
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
              'n', 'ñ', 'o', 'p', 'q', 'r', 's','t', 'u', 'v', 'w', 'x', 'y', 'z']
    codigo = ''
              
    for i in range(cant_digitos):
        elegido = choice(letras)
        while elegido in codigo:        
            elegido = choice(letras)            
        codigo += elegido
        
    print('Tienes que adivinar un codigo de', cant_digitos, 'digitos distintos')
    propuesta = input('Que codigo propones?: ')

    intentos = 1
    while propuesta != codigo:
        intentos += 1
        aciertos = 0
        coincidencias = 0
        for i in range(cant_digitos):
            if propuesta[i] == codigo[i]:
                aciertos += 1
            elif propuesta[i] in codigo:
                coincidencias += 1
        print('Tu propuesta', propuesta, 'tiene', aciertos, 'aciertos y', coincidencias, 'coincidencias')
        propuesta = input('Propon otro codigo: ')
        
    print('Felicidades adiovinaste el codigo en', intentos, 'intentos')
    continuar = int(input('Desea seguir jugando? 1 = si, 0 = no: '))