# Author: 
#          A01379896 Erick Bautista Pérez
#
#Write a program called pyramid.py. Define in this program a function pyramid(n) 
#that returns 12 + 22+ 32 + ... + n2. The program’s main() function should print 
#a table with the values of pyramid(n) for n = 1, 2, 3, ..., 20.
#
# September 7, 2016.

#n**2+n**2
def pyramid(n):
    s=0  
    for i in range(1, n+1):    
        s= s+i**2
    return s

def main():
    for i in range(1,21):
        print(i, pyramid(i))
    
main()


