# Authors: 
#         A01379896 Erick Bautista Pérez
#Write a program called triangles.py. Define in this program a function called 
#triangle_kind(x1, y1, x2, y2, x3, y3). The six input parameters correspond to 
#three points on a two-dimensional coordinate plane: (x1, y1), (x2, y2), and (x3, y3). 
#Assume the three points are connected in order to form a triangle. The function should 
#return a string indicating what kind of triangle they formed: 'right', 'equilateral', 
#'isosceles', or 'scalene'.
from math import sqrt, isclose

def sort3(x, y, z):
    a = x
    b = y
    c = z    
    if  a <= b and b <= c:
        return a, b, c   
    elif a <= c and c <= b:
        return a, c, b
    elif b <= a and a <= c:
        return b, a, c    
    elif b <= c and c <= a:
        return b, c, a    
    elif c <= a and a <= b:
        return c, a, b
    elif c <= b and b <= a:
        return c, b, a
    else:
        return c

def distancia(x1, y1, x2, y2):
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

def triangle_kind(x1, y1, x2, y2, x3, y3):
    a = distancia(x1, y1, x2, y2)
    b = distancia(x1, y1, x3, y3)
    c = distancia(x2, y2, x3, y3)    
    a, b, c = sort3(a, b, c)
    if isclose(a ** 2 + b ** 2, c ** 2):
        return "right"
    elif isclose(a, b) and isclose(b, c):
        return "equilateral"
    elif isclose(a, b) or isclose(a, c) or isclose(b,c):
        return "isosceles"
    else:
        return "scalene"

def main():
    print(triangle_kind(1, 2, 2, 3, 4, 2))
    print(triangle_kind(1, 1, 2, 3, 3, 1))
    print(triangle_kind(1, 3, 1, 5, 1 + sqrt(3), 4))
    print(triangle_kind(5, 5, 3, 5, 3, 1))

main()    