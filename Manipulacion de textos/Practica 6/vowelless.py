# Authors: 
#           A01379896 Erick Bautista Pérez
# Write a program called vowelless.py. Define in this program a function called 
#vowelless(word) that returns a new string that contains the exact same characters contained 
#in word but without any vowels. 
#
# October 14, 2016.

def vowelless(word):
    resultado = ""
    for c in word:
        if c not in "AEIOUaeiou":
            resultado += c
    
    return resultado
    
def main():
    print(vowelless('<AEIOUaeiou>'))
    print(vowelless('Hello!'))
    print(vowelless('This is a little test.'))
    print(vowelless('UMPA-LUMPA'))
    
    
main()
    