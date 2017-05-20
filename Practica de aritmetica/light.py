# # Authors: 
#          A01379896 Erick Bautista Pérez
#          A01378568 Leonardo Valencia Benitez
# August 31, 2016.

#Light travels 299,792,458 meters per second. A light-year is the distance a 
#light beam travels in one year. Write a program called light.py that 
#calculates and displays the value (in meters) of a light-year 
#(assume that a year has 365.25 days).
#Sacar el valor de un año en segundos de un año luz

light=299792458 #meters per second
age=365.25 #days
day=24 #hours
hour=60 #minutes
minute=60 #seconds

B=int(light*age*day*hour*minute)

print("The value of light-year in seconds is", B, "meters")