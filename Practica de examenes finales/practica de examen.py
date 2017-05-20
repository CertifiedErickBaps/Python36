# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 16:57:39 2016

@author: Erick
"""
#def uno(n):
#    lista = []
#    lista.append(n)
#    for i in lista:    
#        n = lista[-1]
#        if int(n) == 1:
#            return lista
#        elif int(n) % 2 == 0:
#            b = n // 2
#            lista.append(b)
#        elif int(n) % 2 != 0:
#            a = (n * 3) + 1
#            lista.append(a)
#        
#    return lista
#    
#    
#    
#def main():
#    print(uno(22))
#    print(uno(1))
#    print(uno(14))
#    print(uno(1024))
#main()

#def dos(n):
#    letras1 = 'QWERTYUIOPASDFGHJKLZXCVBNM'
#    letras = letras1.lower()
#    par = 0
#    impar = 0 
#    for i in n:
#        if i in letras1:
#            par += 1
#        elif i in letras:
#            impar += 1
#    #print(impar, par)
#    if par == impar:
#        return True
#    else:
#        return False
#            
#     
#def main():
#    print(dos('HoLa'))
#    print(dos('ADios'))
#    print(dos('CoNTRaRREvoLucionARIos'))
#    print(dos('moroLongo'))
#main()

#def tres(entrada, salida):
#    with open(entrada, 'r') as f:
#        f = f.readlines()
#        
#    with open(salida, 'w') as a:
#        lista = []
#        for i in f:
#            espacios = i.rstrip()
#            lista.append(int(espacios))
#
#        codigo = ''        
#        for c in lista:
#            w = c * '*'
#            codigo2 = codigo + (w + '\n') * c
#            codigo = codigo2 + '\n'
#        a.write(codigo)
#    
#def main():
#    tres('entrada.txt', 'salida.txt')
#main()

#def uno(s):
#    lista = list(s.split())
#    #print(lista)
#    iniciales = ''
#    for i in lista:
#        iniciales += i[0]
#
#    letra = s[0]
#    if letra.lower() * (len(lista)) == iniciales.lower():
#        return True
#    else:
#        return False
#
#
#
#def main():
#    print(uno("Mi mama me mima mucho."))
#    print(uno("Para poder Presumir, Practica previamente."))
#    print(uno("Pepe pecas pica papas con un pico."))
#    print(uno("Erre con erre cigarro, erre con erre barril."))
#main()

#def dos(m, n):
#    resultado = 0   
#    for i in range(m):
#        if m != 0:
#            residuo = m % 10
#            m //= 10
#            resultado = resultado * 10 + residuo
#    
#    resultado2 = 0
#    while n != 0:
#        residuo = n % 10
#        n //= 10
#        resultado2 = resultado2 * 10 + residuo
#
#    return resultado2 + resultado
#    
#    
#    
#    
#def main():
#    print(dos(123, 5019))
#    print(dos(10, 100))
#    print(dos(100000, 23))
#    print(dos(42, 23))
#main()

#def tres(entrada, salida):
#    with open(entrada, 'r') as f:
#        f = f.readlines()
#        
#    with open(salida, 'w') as a:
#        c = '' 
#        x = ''
#        
#        for linea in f:
#            c = int(linea)
#            for i in range(1, c + 1):
#                t = i * '*' + '\n'
#                x = t + '\n'
#                a.write(x)
#                
#                
#    
#def main():
#    tres('entrada.txt', 'hola.txt')
#main()