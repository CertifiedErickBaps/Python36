
#Erick Bautista Pérez
#Description
#Bessie is tired of multiplying pairs of numbers the usual way, so she invented 
#her own style of multiplication. In her style, A*B is equal to the sum of all 
#possible pairwise products between the digits of A and B. For example, the product 
#123*45 is equal to 1*4 + 1*5 + 2*4 + 2*5 + 3*4 + 3*5 = 54. Given two integers A and B 
#(1 ≤ A, B ≤ 1,000,000,000), determine A*B in Bessie's style of multiplication.
from __future__ import print_function
from __future__ import division

from sys import stdin

entrada = stdin.read().split()

def bessie(a,b):
    suma = 0
    for a in entrada[0]:
        for b in entrada[1]:
            x = int(a)
            y = int(b)
            suma += x*y
            print(x, y)
    print(suma)
    
    
    
#def Bessie(a, b):
#    resultado = 0    
#        while a != 0:
#            residuo = a % 10
#        a //= 10 
#        
#        
#        
#        
def main():
    print(bessie(123, 45))
main()

 
