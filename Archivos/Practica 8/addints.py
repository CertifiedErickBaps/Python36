# Authors: 
#          A01379896 Erick Bautista Perez
#
#Write a program called addints.py. Define in this program a function called addints(infile) 
#that takes one argument: a string with the name of the input file infile that contains a 
#sequence of integer numbers, each number in its own line. The function should return the 
#result of adding all these integers together.
#
# November 4, 2016.

def addints(infile):
    with open(infile) as f:
        c = 0 
        for z in f:
            c += int(z) #Para poder convertir a un numero 
        return c

def main():
    print(addints('numbers.txt'))
    
main()