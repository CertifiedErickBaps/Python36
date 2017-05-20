# Authors: 
#          A01379896 Erick Bautista Pérez
#          A01378568 Leonardo Valencia Benitez
# August 31, 2016.
#Write a program called nautical.py that takes as input a number of kilometers 
#and prints the corresponding number of nautical miles. Use the following 
#approximations:
#A kilometer represents 1/10,000 of the distance between the North Pole and the equator.
#There are 90 degrees between the North Pole and the equator.
#One degree is equal to 60 arcminutes.
#One nautical mile is equal to one arcminute.

A=float(input("Number of kilometers: ")) #La formula es (1/10000)*90*60*Numero de kilometros deseados.

kilometer=1/10000
grades=90
arcminutes=60
Nautical_mile=(kilometer)*grades*arcminutes*A

print(A, "kilometers is equal to ", Nautical_mile, "nautical miles." )