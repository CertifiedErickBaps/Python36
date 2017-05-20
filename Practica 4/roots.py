# Authors: 
#         A01379896 Erick Bautista Pérez
#
#Given a quadratic equation ax2+bx+c, we define its discriminant as:
#If the discriminant is a positive number greater than zero, the quadratic equation 
#has two real roots. If the discriminant is equal to zero, the quadratic equation has one real root. 
#Finally, if the discriminant is a negative number, the quadratic equation has no real roots.
#
#Write a program called roots.py. Define in this program a function called numroots(a, b, c) 
#that returns the number of real roots (0, 1, or 2) for a quadratic equation given its coefficients 
#a, b, and c. Use the following main() function to test your numroots() function:
#
# September 23, 2016.

def numroots(a, b, c): 
    w = (b**2) - (4*a*c)

    if w > 0:
        return 2
    if w == 0:
        return 1
    else:
        return 0
            
def main():
    print(numroots(4, 5, 1))
    print(numroots(2, 4, 2))
    print(numroots(1, 2, 3))
                
main()