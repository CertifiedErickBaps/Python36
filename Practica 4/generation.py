# Authors: 
#         A01379896 Erick Bautista Pérez
#
#Write a program called generation.py. 
#Define in this program a function called generation(y) 
#that returns a string indicating the generation to which a person 
#belongs given the year y in which she was born. Use the information 
#in this table:
# September 23, 2016.

def generation(y):
    if  y <= 1945:
        return "Mature"
    elif 1946 <= y <= 1964:
        return "Baby Boomer"
    elif 1965 <= y <= 1980:
        return "Generation X"
    elif 1981 <= y <= 2000:
        return "Millenium"
    else:
        return "Boomlet"
        
def main():
    for i in range(1945, 2006, 5):
        print(i, generation(i))
        
main()
    