# Authors: 
#          A01379896 Erick Bautista Pérez
#          A01378568 Leonardo Valencia Benitez
# August 31, 2016.

#Description: Five Star Video rents new videos for $3.00 a night, and oldies for $2.00 a night.
#Write a program called video.py that the clerks at Five Star Video can use to calculate
#the total charge for a costumer’s video rentals. The program should prompt the user for
#the number of each type of video and output the total cost.

A=int(input("Number of new videos to rent: "))
B=int(input("Number of old videos to rent: "))

C= A*3.00
D= B*2.00
E= int(C+D)

print("Total charge for costumer's video rentals: $", E)