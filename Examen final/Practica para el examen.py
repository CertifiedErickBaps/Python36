#Practica para el examen

#def mul(k, x):
#    s = []
#    for c in x:
#        a = (c * k)
#        s += [a]
#    return s
#    
#def main():
#    print(mul(3, [4, 3, 1, 5]))
#    print(mul(0, [1, 2, 3, 4]))
#    print(mul(7, []))
#    print(mul(108, [4, 8, 15, 16, 23, 42]))
#main()
#==============================================================================

#def sumadig(entrada):         
#    with open(entrada) as texto:
#        texto = texto.read() #Lee el texto
#        a = texto.split() #Separa por palabras
#        b = '' #El acumulador esta aqui
#        d = 0  #Acumulador para suma  
#        for c in a:
#            b += c #Se usa aqui el acumulador de b
#        for x in b:
#            if x.isdigit(): #Si el cararter es un numero se cumplira el cuerpo del if
#                d += int(x) #Tienes que comvertir el caracter a numero para poder sumarse entre los demas
#        return d
#            
#def main():
#    print(sumadig('poema.txt'))
#main()
#==============================================================================

#def fibarchivo(n, salida):
#    with open(salida, 'w') as f:
#        a = 0
#        b = 1
#        for k in range(1, n + 1):
#            i = a + b
#            b = a
#            a = i
#            f.write(str(b) + '\n')
#            
#def main():
#    fibarchivo(10, 'fibos.txt')
#main()
#==============================================================================
#def words(outfile, s):
#    with open(outfile, 'w') as f:
#        s = s.split() # Solo se usa split para archivos 
#        for c in s:       
#            f.write(str(c) + '\n')
#
#def main():    
#    words("output.txt", "I'm gonna make him an offer he can't refuse")
#
#main()
#==============================================================================
#def add(a,b):
#    s = []
#    for c in range(len(a)):
#        s.append(a[c] + b[c])
#    return s
#    
#    
#    
#def main():
#    print(add([1, 2, 3], [4, 5, 6]))
#    print(add([1, 1, 1, 2], [2, 2, 2, 1]))
#    print(add([15, 2, -4, 7, 2, -14, 24, -22, 3, -16, 6, -17, -3, -3, -23],
#              [-14, 0, 7, -3, 3, 20, -17, 30, 6, 26, 5, 29, 16, 17, 38]))
#main()    
#==============================================================================
#
#def countv(infile):
#    with open(infile) as f:
#        f = f.read() #Primero se lee todo el texto
#        s = ''       #Acumulador para todo el texto 
#        vocales = 'aeiouAEIOU' 
#        a = 0 #El acumulador para saber cuantas vocales hay
#        for c in f:
#            s += c #Acumulador del todo el texto
#        for x in s:# Este for va caracter por caracter
#            if x in vocales:
#                a += 1 #Suma las vocales
#        return a
#                
#            
#def main():
#    print(countv('hanging.txt'))
#main()
##
    