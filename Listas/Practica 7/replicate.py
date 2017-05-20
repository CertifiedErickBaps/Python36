# Authors: 
#          A01379896 Erick Bautista Perez
#
#Write a program called replicate.py. Define in this program a function called replicate(n, x) 
#that takes two arguments: a list x and an integer number n, where n ≥ 0. It returns a new list 
#that replicates n times each element contained in x.
# October 28, 2016.


def replicate(n,x):
    d = []
    for i in x:
        if n >= 0:        
            b = n * [i]
            d += b
            
    return d

def main():
    print(replicate(7, []))
    print(replicate(0, ["a", "b", "c"]))
    print(replicate(3, ["a", "b", "c"]))
    print(replicate(4, [1, 2, 3, 4]))
main()