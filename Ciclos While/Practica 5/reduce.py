# Authors: 
#          A01379896 Erick Bautista Pérez
#
#Write a program called reduce.py. Define in this program a function called reduce(n) that reduces the value of n. 
#The reduction consists in adding up all individual digits of the given number and repeating this process until you 
#get a one digit number. For example, reduce(897) would first add 8 + 9 + 7 = 24; because 24 is not a one digit number 
#the process has to be repeated: 2 + 4 = 6; given that 6 is a one digit number, that’s the result that should be returned by the reduce() function.
# October 7, 2016.
def suma_digitos(n):
    r = 0
    while n != 0:
        residuo = n % 10
        n //= 10
        r += residuo
    return r    

def reduce(n):
    while n > 10:   
        n = suma_digitos(n)  
    return n
    
def main():
    print(reduce(897))
    print(reduce(67521))
    print(reduce(10000))
    print(reduce(9999999999999))
    print(reduce(123456789123456789123456789123456789))
    
    
main()

