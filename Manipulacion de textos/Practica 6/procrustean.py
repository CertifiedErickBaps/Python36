# Authors: 
#           A01379896 Erick Bautista Pérez
#Procrustes was a legendary robber of ancient Attica. He bound his victims to a bed, and if they were shorter 
#than the bed, he stretched their limbs until they would fit; if their limbs were longer, he chopped them off.

#Write a program called procrustean.py. Define in this program a function called procrustean(string, size, padding) 
#that takes string and “procrusteans” it to size number of characters, using padding if necessary. This means that 
#if string has a length greater than size, the function should return the original string truncated to size 
#characters. On the other hand, if the length of string is less than size, the function should return string 
#concatenated to padding repeated as many times as necessary in order to produce a resulting string with exactly 
#size characters. Lastly, if string has a length which happens to be equal to size, the function should return 
#string with no alterations.

# October 14, 2016.

def procrustean(string, size, padding):
    while len(string) < size:
        string += padding
    if len(string) > size:
        string = string[:size]
    return string
def main():
    print(procrustean('Hello', 10, '*'))
    print(procrustean('Hello world!', 10, '*'))
    print(procrustean('Hello', 5, '*'))
    print(procrustean('AB', 20, 'test'))
main()    
        