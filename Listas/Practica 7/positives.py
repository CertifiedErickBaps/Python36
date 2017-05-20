# Authors: 
#          A013979896 Erick Bautista Perez
#
#Write a program called positives.py. Define in this program a function called 
#positives(x) that takes a list of numbers x as its argument, and returns a new 
#list that only contains the positive numbers of x. 
#
# October 28, 2016.

def positives(x):
    a = []
    for c in x:
        if c >= 0:
            a += [c]
    return a 
        
        
def main():
    print(positives([-21, -31]))
    print(positives([-48, -2, 0, -47, 45]))
    print(positives([-9, -38, 49, -49, 32, 6, 4, 26, -8, 45]))
    print(positives([-27, 48, 13, 5, 27, 5, -48, -42, -35, 49,
                     -41, -24, 11, 29, 33, -8, 45, -44, 12, 46]))
    print(positives([-2, 0, 27, 47, -13, -23, 8, -28, 23, 7,
                     -29, -24, -30, -6, -21, -17, -35, -8, -30,
                     -7, -48, -18, -2, 1, -1, 18, 35, -32, -42,
                     -5, 46, 8, 0, -31, -23, -47, -4, 37, -5,
                     -45, -17, -5, -29, -35, -2, 40, 9, 25, -11,
                     -32]))
main()