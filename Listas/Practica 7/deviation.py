# Authors: 
#          A01379896 Erick Bautista Perez
#
#In statistics, the standard deviation σ is a measure of how spread out numbers are. It has the following formula:
#Where x is the arithmetic mean and is defined as follows:
#Write a program called deviation.py. Define in this program a function called deviation(x) that returns the standard deviation of the list of numbers contained in x.
# October 28, 2016.
from math import sqrt

def media(x):
    return sum(x) / len(x)

def deviation(x):
    m = media(x)
    s = 0
    for e in x:
        s += (e - m)**2
    s /= len(x)
    return sqrt(s)

def main():
    print(deviation([42]))
    print(deviation([10, 20]))
    print(deviation([1, 2, 3, 4, 5]))
    print(deviation([7, 7, 7, 7, 7, 7, 7]))
    print(deviation([32, 88, 20, 26, 14, 24, 26, 44, 14, 94, 94, 72, 
                     8, 46, 92, 50, 38, 56, 60, 84]))
                     
main()
#Usando indices
#def suma(x):
#    s = 0
#    for i in range(len(x)):
#        s += x[i]
#    return s

#Sin usar indices
#def suma(x):
#    s = 0
#    for e in x:
#        s += e
#    return s
        
        
        
        
        
        