# Authors: 
#           A01379896 Erick Bautista Pérez
# A palindrome is a word or sequence that reads the same backward as forward. 
#For example: ana, civic, or madam. Write a program called palindrome.py. 
#Define in this program a function called palindrome(s) that returns True if s is a palindrome, 
#otherwise returns False.
#
# October 14, 2016.

def palindrome(s):
    for c in s:
        if s == s[::-1]: #El valor de s[::-1] es el valor inverso y nos mostrara si es igual el valor dado 
            return True
        else:
            return False

def main():
    print(palindrome("ana"))
    print(palindrome("civic") and palindrome("madam"))
    print(palindrome("sexes madam sexes"))
    print(palindrome("what is this?"))
    print(palindrome("not a palindrome"))
    print(palindrome("annas") or palindrome("caiaphas"))
main()