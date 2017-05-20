# Author: 
#          A01379896 Erick Bautista Pérez
#
#Write a program temptable.py. The program should contain a function called fahrenheit_to_celsius(x) 
#that converts x degrees Fahrenheit to its equivalent degrees Celsius. Remember that:
#°C = (5 / 9)(°F - 32)
#The main() function should print a table for temperatures between –30°F and 100°F at 10 degree intervals, 
#with their corresponding conversion to degrees Celsius as returned by the fahrenheit_to_celsius(x) function.
#
# September 7, 2016.

def fahrenheit_to_celsius(x):
    #return (5/9)*(x-32)  sale lo mismo pero mas corto   
    x = (5/9)*(x-32)
    return x
    
def main():
    for i in range(-30,110,10): #tambien se usaria un 101 para que llegue al 100
        print(i,"°F=", fahrenheit_to_celsius(i), "°C") #primero se da el valor de i que son los F
        #Luego se da la funcion definida de celsius(i)= lo que me da F 

main()