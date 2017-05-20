#numbers.py
#def main():
#    print ("Un ejemplo es calcular el promedio de grado, \ncomo se muestra a continuación:\n")
#
#    promedio = 0.0
#    total = 0
#    contar = 0
#    
#    print ("Introduzca valor numerico de un grado (-1 para salir): ")
#    grado = int(input())	
#    while grado != -1:
#        total = total + grado
#        contar = contar + 1
#        print ("Introduzca valor numerico de un grado (-1 para salir): ")
#        grado = int(input())
#    promedio = total / contar
#    print ("Promedio de grado: " + str(promedio))
#main()
#-------------------------------------------------------------------------

#x = "a" + (4*"b")
#print(x)

#-------------------------------------------------------------------------

#print("x" in "LOL")
#s = " "
#for i in range(3):
#    s += "t" + str(i)
#print(s)

#-------------------------------------------------------------------------

#From math import ceil
#funcion techo ceil(3.0)
#-------------------------------------------------------------------------

#from math import ceil
#def procrustean(string, size, padding):
#    if len(string) < size:
#       n = ceil((size - len(string)) / len(padding))
#       string += padding * n
#       return string
#def main():
#    print(procrustean('Hello', 10, '*'))
#    print(procrustean('Hello world!', 10, '*'))
#    print(procrustean('AB', 20, 'test'))
#main()    

#-------------------------------------------------------------------------

#def main():
#    r = int(input("Escriba un numero: "))
#    x = int(input("Escribe un numero mayor que " + str(r) + ": "))    
#    while x <= r:
#        
#        print(x, "no es mayor que", str(r) ,". Intentelo de nuevo: ", end="")
#        x = int(input())
#        
#    print("Los numeros que ha escrito son", r, "y", str(x))
#    print("Programa terminado")
#    
#main()
#-------------------------------------------------------------------------

#\n  Newline.
#\t  Tab.
#\"  To get " inside a double-quoted string.
#\’  To get ’ inside a single-quoted string.
#\\  If you need a backslash itself.
#chr(n)  Character with ASCII code n.
#ord(c)  ASCII code for the character c.
#len(x)  Number of elements in x.
#min(x)  Smallest element in x.
#max(x)  Largest element in x.

#-------------------------------------------------------------------------

#def main():
#    r = int(input("Escriba un numero: "))
#    x = int(input("Escribe un numero mayor que " + str(r) + ": "))    
#    while x > r:
#        if x < r:
#            break
#        x = int(input("Escriba otro numero mayor que " + str(r) + ": "))
#    print(x, "no es mayor que", r,"\nPrograma terminado.\nLos numeros que ha escrito son", r, "y", str(x))
#main()

#-------------------------------------------------------------------------

#def fib2(n):  # return Fibonacci series up to n
#     #"""Return a list containing the Fibonacci series up to n."""
#     result = ""
#     a, b = 0, 1
#     while a < n:
#         result += str(a)   # see below
#         a, b = b, a+b
#     return result
#def main():
#    print(fib2(100))
#main()

#-------------------------------------------------------------------------
#def euclides(a, b):
#    resultado = 0    
#    while a % b:
#        resultado += (a % b)
#        if resultado == 0:
#            return resultado
#            break
