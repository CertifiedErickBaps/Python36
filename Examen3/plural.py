#Erick Bautista Perez A01379896
def plural(palabra):
    r = ""    
    if palabra[-1] in "aeiou":
        r = palabra + "s"
    elif palabra[-1] in "z":
        r = palabra[:-1] + "ces"
    else:
        r = palabra + "es"
    return r
# len(s) nos dara un 4 en gato 
## s[len(s)-1] == s[-1]         
#def plural(palabra):
#    c = palabra[-1]    
#    if c in "aeiou":
#        return palabra + "s"
#    elif c == "z":
#        return palabra[:-1] + "ces"
#    else:
#        return palabra + "es"
#        
def main():
    print(plural("gato"))
    print(plural("puerta"))
    print(plural("zopilote"))
    print(plural("nuez"))
    print(plural("codorniz"))
    print(plural("cruz"))
    print(plural("animal"))
    print(plural("complot"))
    print(plural("hobits"))
main()
            