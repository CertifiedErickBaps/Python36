# Authors: 
#          A01379896 Erick Bautista Perez
#
#The Fibonacci sequence is:
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
#The sequence starts with 0 and 1. Any number that follows is calculated by adding the previous two numbers.
#Write a program called fibo.py. Define in this program a function called fibo(n) that returns a list with the 
#first n Fibonacci numbers.
# October 28, 2016.

def fibo(n):
    r = []
    a = 0
    b = 1
    for k in range(1, n + 1):
        i = a + b
        b = a
        a = i
        r.append(b)
    return r
def main():
    print(fibo(0))
    print(fibo(1))
    print(fibo(2))
    print(fibo(5))
    print(fibo(10))
    print(fibo(30))
    print(fibo(100))
    
main()