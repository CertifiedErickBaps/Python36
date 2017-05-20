# Authors: 
#          A01379896 Erick Bautista Perez
#
#Write a program called compress.py. Define in this program a function called compress(x) 
#that takes a list x as its argument. If x contains consecutive repeated elements, they should 
#be replaced with a single copy of that element. The order of the elements should not be changed.
# October 28, 2016.


def compress(x):
    r = []    
    ultimo = None#Representa ningun valor en particular    
    for i in x:
        if i != ultimo:
            r.append(i) #agregamos la i
            ultimo = i
    return r #importante poner el return alineado con el for, si lo pones dentro del if solo te dara el primer valor 
    
def main():
    print(compress(['a', 'a', 'a', 'a', 'b', 'c', 'c', 'a', 'a', 'd',
                    'e', 'e', 'e', 'e']))
    print(compress(['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']))
    print(compress(['a', 'b', 'c', 'd']))
    print(compress([]))
main()