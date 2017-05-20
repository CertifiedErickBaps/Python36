# Authors: 
#          A01379896 Erick Bautista Pérez
#Write a program called basel.py. Define in this program a function called 
#basel(n) that calculate the following series:
#
# September 7, 2016.

def basel(n):
    s=0 # se refiere a una suma
    for k in range(1, n+1):
        s += (1/(k**2))
    return s
    
def main():
    for i in range(1, 8):
        m=(10**i)
        print(m, basel(m))#Separa elementos de un espacio
        
main()