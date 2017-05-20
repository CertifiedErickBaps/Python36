# Authors: 
#          A01379896 Erick Bautista Pérez
#          A01378568 Leonardo Valencia Benitez
# August 31, 2016.

# An object’s momentum is its mass multiplied by its velocity. 
#Write a program called momentum.py that accepts an object’s mass (in kilograms) 
#and velocity (in meters per second) as inputs and then outputs its momentum.

A=float(input("Object's mass in kilograms: "))
B=float(input("Object's velocity in meters per second: "))

C= A*B
print("The object's momentum is: ", C,"kg m/s")