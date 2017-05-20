# Authors: 
#          A01379896 Erick Bautista Pérez
#          A01378568 Leonardo Valencia Benitez
# August 31, 2016.

#The kinetic energy of a moving object is given by the formula:
#KE = (1/2)mv2
#Where m is the object’s mass and v is its velocity. Write a program called kinetic.py 
#that prints the object’s kinetic energy as well as its momentum (see the previous problem).

A=float(input("Object's mass in kilograms: " ))
B=float(input("Objec's velocity in meters per second: "))

C= A*B
D=(1/2)*A*B**2


print("The object's kinetic energy is: ", D, "joules")
print("The objetc's momentum is: ", C, "kg m/s")