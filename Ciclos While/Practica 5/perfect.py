# Authors: 
#          A01379896 Erick Bautista Pérez
#According to Wikipedia: “a perfect number is a positive integer that is equal to the sum of its proper positive divisors, that is, the sum of its positive divisors excluding the number itself”. For example, 28 is a perfect number because the proper divisors of 28 are: 1, 2, 4, 7, and 14; and 1 + 2 + 4 + 7 + 14 = 28.

#Write a program called perfect.py. Define in this program a function called perfect(n) that returns 
#True if n is a perfect number, otherwise returns False.
# October 7, 2016.

def perfect(n):
    x = 0   
    for i in range(1, n):
        if n % i == 0:
            x += i
    if n == x:
        return True 
    else:
        return False


def main():
    for i in range (1, 10000):
        if perfect(i):          #El ultimo numero perfecto tarda bastante
            print(i)
main()
