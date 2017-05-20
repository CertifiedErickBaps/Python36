from math import pi, factorial
def pi_aprox(n):
    s = 0
    for i in range(n+1):
        s += (-1) ** i / (2 * (i) + 1)
    return s * 4
    
def coseno_aprox(x, n):
    s = 0
    for i in range(n + 1):
        s += ((-1) **i) * (x ** (2*i)) / (factorial(2*i))
    return s



def main():
    print(pi_aprox(1000))
    print(pi)    
    print(coseno_aprox(0, 10))
    print(coseno_aprox(pi, 20))
    print(coseno_aprox(pi/2, 20))
    print(coseno_aprox(pi/3, 20))
main()