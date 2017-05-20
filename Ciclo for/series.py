from math import pi, factorial, e

def pi_aprox(n):
    s = 0 #si s no existiera no podria ser la formula de la linea 6
    for i in range(n + 1):
        s += (-1) ** i/ (2 * i + 1) #siempre poner parentesis cuando sea negativo el valor, tambien parentesis por jerarquia de operaciones
    return s * 4 #Para que me de pi

def coseno(x, n):
    s = 0
    for i in range(n + 1):
        s += ((-1) ** i * x ** (2 * i))/ factorial(2 * i) #Es importante poner los parentesis
    return s #Va afuera del for, si no pones este return solo se asigna el 0 a toda la formula :c

def e_aprox(x, n):
    s = 0
    for i in range(n + 1): #Tambien podemos poner 0, n+1
        s += (x ** i) / (factorial(i))
    return s

def main():
    print(pi)
    print(pi_aprox(100)) # Cada vez que se agrande con un 0 se dara un valor aproximado de pi
                            #Este print es solo para ver que existe una formula para acercarse a pi
    print(coseno(0, 10))
    print(coseno(pi, 20)) #le agregamos un valor de 20 en vez del 10 para que se pueda acerca a un valor de -1
    print(coseno(pi/2, 20))
    print(coseno(pi/3, 20))
    print(e_aprox(1, 10))
    print(e)
main()

