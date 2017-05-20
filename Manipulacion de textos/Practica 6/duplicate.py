# Authors: 
#           A01379896 Erick Bautista Pérez
# Write a program called duplicate.py. Define in this program a function called duplicate(s) 
#that returns a new string in which every character of s is duplicated. For example, duplicate("Hello") 
#should return "HHeelllloo"
#
# October 14, 2016.

def duplicate(s):    
    x = ""
    for c in s:
        x += 2*c
    return x
    
def main():
    print(duplicate("Hello"))
    print(duplicate(""))
    print(duplicate("Programming is fun!"))
    print(duplicate("THE END"))
main()    