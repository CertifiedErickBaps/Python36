# Authors: 
#           A01379896 Erick Bautista Pérez
#Write a program called username.py. Define in this program a function called username(first, middle, last) 
#that takes the first name, middle name, and last name of a person and generates her user name given the above 
#rules. You may assume that every first name has at least one letter and every middle name has at least one 
#consonant. Use string.lower() to convert string into lower case letters.
#
# October 14, 2016.

#def first(name):        
#    for c in name:
#        if name != "":
#           return str.lower(name[:1])
            
#def middle(name1):
#    for a in name1:
#        if a not in "AEIOUaeiou":
#            return str.lower(a)

#def last(name2):
#    if name2 < name2[0:6]:
#        return str.lower(last)
#    else:
#        return str.lower(name2[0:6])

#def main():
#    print(first('Scarlett'), middle('Ingrid'), last('Johansson'), sep ="")
#    print(first('Donald'), middle('Ervin'), last('Knuth'), sep ="")
#    print(first('Alan'), middle('Mathison'), last('Turing'), sep ="")
#    print(first('Martin'), middle('Luther'), last('King'), sep ="")
#    print(first('Stephen'), middle('William'), last('Hawking'), sep ="")
#    print(first('Alejandro'), middle('Gonzalez'), last('Inarritu'), sep ="")   
#main()
def primera_consonante(cadena):
    for c in cadena.lower(): # .lower() es para regresar el valor en minusculas
        if c in "bcdfghjklmnpqrtsvwxyz":
            return c #en este return acaba inmediatamente y regresa la consonante
            
def username(first, middle, last):
    resultado = first[0]
    resultado += primera_consonante(middle)
    resultado += last
    if len(resultado) > 8:        #El len() me regresa el numero de caracteres
        resultado = resultado[:8]
    resultado = resultado.lower() #Este resultado esta fuera del if por que es una condicion a llamar con el tamaño
    return resultado
    
def main():
    print(username('Scarlett', 'Ingrid', 'Johansson'))
    print(username('Donald', 'Ervin', 'Knuth'))
    print(username('Alan', 'Mathison', 'Turing'))
    print(username('Martin', 'Luther', 'King'))
    print(username('Stephen', 'William', 'Hawking'))
    print(username('Alejandro', 'Gonzalez', 'Inarritu'))
main()    
    
    
    
    
    