# Authors: 
#          A01379896 Erick Bautista Pérez
#          A01378568 Leonardo Valencia Benitez
#
# August 31, 2016.
#An employee’s total weekly pay equals the hourly wage multiplied by the total 
#number of regular hours plus any overtime pay. Overtime pay equals the total 
#overtime hours multiplied by 1.5 times the hourly wage. Write a program called 
#wage.py that takes as inputs the hourly wage, total regular hours, and total 
#overtime hours and displays an employee’s total weekly pay.

A=float(input("Hourly wage: "))
B=float(input("Total regular hours: "))
C=float(input("Tota overtime hours: "))

D=A*B+(C*(1.5*A))

print("Employee's total weekly pay is: $", D)