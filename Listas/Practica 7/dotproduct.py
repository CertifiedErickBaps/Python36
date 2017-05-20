# Authors: 
#          A01379896 Erick Bautista Perez
#
#Write a program called dotproduct.py. Define in this program a function called 
#dotproduct(a, b) that takes two arguments: the lists a and b. It returns the result 
#of performing the dot product of a times b. The dot product is an algebraic operation 
#that takes two equal-length sequences of numbers and returns a single number obtained 
#by multiplying corresponding entries and then summing those products:
#
# October 28, 2016.
def dotproduct(a,b):
    s = 0
    for i in range(0, len(a)):
        c = a[i]
        d = b[i]
        s += (c * d) 
    return s  
    
def main():
    print(dotproduct([], []))
    print(dotproduct([1, 2, 3], [4, 5, 6]))
    print(dotproduct([1.3, 3.4, 5.7, 9.5, 10.4],
                     [-4.5, 3.0, 1.5, 0.9, 0.0]))
    print(dotproduct([92, -39, 82, 16, -64, -1, -16, -45, -7,
                      39, 45, 0, 34, -3, -51, 71, 23, -8, 41, -40],
                     [-50, -81, 94, -84, 47, 86, 52, 19, -57, 36,
                      -20, 11, -42, 48, 14, 13, 9, -67, 92, 96]))
main()