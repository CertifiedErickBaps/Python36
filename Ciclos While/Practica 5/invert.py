# Authors: 
#          A01379896 Erick Bautista Pérez
#
#Write a program called invert.py. Define in this program a function called invert(n) 
#that returns an integer comprised of the same digits contained in n but in reversed order. 
#For example, invert(2015) should return the number 5102. Do not use any string operations to 
#solve this problem.
# October 7, 2016.
def invert(n):
    resultado = 0    
    while n != 0:
        residuo = n % 10
        n //= 10
        resultado = resultado * 10 + residuo #Se puede dejar asi por el orden de las operaciones

    return resultado #Para que regrese el resultado 
def main(): 
    print(invert(2015))
    print(invert(123456789))
    print(invert(1000))
    print(invert(9999))
    print(invert(1234) + 1) 
main()