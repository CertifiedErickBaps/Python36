# Authors: 
#         A01379896 Erick Bautista Pérez
#Write a program called sort3.py. Define in this program a function called sort3(x, y, z) 
#that returns the three values x, y, and z in sorted order (a, b, c), where a ≤ b ≤ c. 
#Do not use any built-in Python sorting functions, but you may put if statements inside of other if statements. 
#The program’s main() function should prompt three values from the user and print them sorted.
# September 23, 2016.

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
                
def main():
    a = int(input("First value: "))
    b = int(input("Second value: "))
    c = int(input("Third value: "))
    print("Sorted values: ", sort3(a, b, c))
    
    
main()