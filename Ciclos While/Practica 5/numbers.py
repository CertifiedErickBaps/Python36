# Authors: 
#          A01379896 Erick Bautista Pérez
#
# Write a program called numbers.py. This program should request the user to input an arbitrary amount of 
#integer numbers. The program should stop requesting more input when the user types a zero. 
#The program should then print how many numbers were typed, and the sum and average of all those numbers 
#(without considering the zero). You do not need to define any functions other than main()
#
# October 7, 2016.

def main():
    Average = 0
    How_many = -1
    Sum = 0
    
    number = int(input("Input an integer number (0 to quit): "))
    while number != 0:
        Sum += number
        How_many += 1
        number = int(input("Input an integer number (0 to quit): "))
    Sum += number
    How_many += 1
    Average = Sum/How_many
    print(How_many ,"numbers were typed.")    
    print("The sum of all those numbers is:", Sum)
    print("The average of all those number is:", Average)
        
        
        
main()
        