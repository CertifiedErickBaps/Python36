# Author: 
#          A01379896 Erick Bautista Pérez
#
#Write a program called table.py 
#that prints a table of values n, log n, n log n, n2, and 2n for n = 10, 20, 30, ..., 200. 
#The log function is in the math module. You do not need to use any functions other than main().
#
# September 7, 2016.
from math import log

def main():
    for i in range(10,210,10 ): 
        print(i, log(i),  i*log (i), i**2, 2**i)
        
main()