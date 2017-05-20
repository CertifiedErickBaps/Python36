# Authors: 
#          A01379896 Erick Bautista Pérez
#          A01378568 Leonardo Valencia Benitez
# August 31, 2016.
#Write a program called rain.py that accepts as input the depth of rain (in inches) 
#that has fallen over an acre of land. The program should calculate and print 
#the water volume (in gallons) accumulated on that acre.

#You will need to use the following conversion formulas:

#1 foot = 12 inches
#1 acre = 43560 square feet
#1 cubic foot = 7.48052 gallons

#Formule: (("A"/12)*acre)*gallons

A=float(input("Depth of rain(in inches): "))

foot=12#inches
acre=43560#square feet
cubic_foot=7.48052#gallons
B=((A/foot)*acre)*cubic_foot

print(A, "inches of rain over one acre of land is equal to", B, "gallons")

