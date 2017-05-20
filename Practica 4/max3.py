# Authors: 
#         A01379896 Erick Bautista Pérez
#Write a program called max3.py. Define in this program a function called max3(x, y, z) 
#that returns the largest of x, y, and z. Do not use the built-in Python function max(). 
#The program’s main() function should prompt three values from the user and print the one that is largest.#
# September 23, 2016.

def max3(x, y, z):
    if x > y or x > z:
        return x
    
    if y > x or y > z:
        return y
        
    else:
        return z
    
       
def main():
    x = int(input("First value: "))
    y = int(input("Second value: "))
    z = int(input("Third value: ")) 
    print("The largest value is:", max3(x, y, z))    
        
main()