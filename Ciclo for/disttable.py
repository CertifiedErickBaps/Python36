# Author: 
#          A01379896 Erick Bautista Pérez
#
#
#Write a program disttable.py that prints a table of mile to kilometer conversions 
#for distances between 100 and 1500 miles at 100 mile intervals. Write a function 
#called miles_to_km(x) to do the conversion. One mile is approximately 1.609 km.
# September 7, 2016.
def miles_to_km(x):
#One mile is approximately 1.609 km.
    One_mile=1.609
    x *= One_mile
    return x

def main():
    for i in range(100,1600,100):
        print(i, "miles =", miles_to_km(i), "km")
        
main()