# Authors: 
#          A01379896 Erick Bautista Pérez
#          A01378568 Leonardo Valencia Benitez
# August 31, 2016.

#In biology, the total population T based on a generation number can be 
#calculated using this formula:
#T = ICn
#Where I is the initial population, C is the number of offspring per parent,
#and n is the generation number. Write a program called population.py 
#that takes I, C, and n as inputs and prints the corresponding total population.

A=int(input("Initial population: "))
B=int(input("Number of offspring per parent: "))
C=int(input("Generation number: "))

D=A*(B**C)

print("Total population is ", D)