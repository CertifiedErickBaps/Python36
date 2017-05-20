# Authors: 
#          A01379896 Erick Bautista Pérez
#
#Write a program called periods.py. Define in this program a funtion called periods(starting, target, interest) 
#that returns the number of investment periods required for the starting balance to have grown equal or larger 
#than the target balance given an interest rate (5% should be specified as 0.05). Although this can be computed 
#directly mathematically, you should use a while loop to solve this problem.
#
#For example, periods(200, 250, 0.05) returns 5, because that’s the number of periods it will take to get to 250 
#(or more) starting with 200 with an 5% interest rate
# October 7, 2016.

def periods(starting, target, interest):
    a = 0 
    while starting < target:
        starting += (starting*interest)
        a += 1
    return a

def main():
    print(periods(200, 250, 0.05))
    print(periods(15000, 14000, 0.07))
    print(periods(15000, 30000, 0.05))
    print(periods(15000, 30000, 0.07))
    print(periods(15000, 30000, 0.10))
    print(periods(15000, 30000, 1.00))
   
main()