# Authors: 
#          A01379896 Erick Bautista Pérez
#
#Write a program called guess.py. The program should pick a random integer number n from 1 to 100. 
#It should then allow the user to guess this number. If the user’s guess is greater or less than n 
#the program should display a message saying so, and then request the user for a new guess; but if 
#the user’s guess is equal to n, the program should end displaying how many tries it took the user 
#to guess correctly. You do not need to define any functions other than main().
# October 7, 2016.
from random import randint

def main():
    How_many = -1   
    r = randint(1, 100)
    print("I'm thinking of a number between 1 and 100.\nTry to guess what number it is.")
    
    number = 0
    while number != r : 
        How_many += 1        
        number = int(input("What's your guess? "))        
        if number > r:
            print ("Your guess is too high")
        if number < r:
            print ("Your guess is too low")
        
    print ("Correct")                
           
    print("It only took you", How_many , "tries")    
    
    
main()
