# area de un cilindro
from math import pi
def area_circulo(radio):# Tiene un parametro
    #area= pi*radio**2 los dos son casi lo mismo o parecido
    return pi*radio**2     #escriba la expresion para regresar a una funcion

def volumen_cilindro(radio, altura):
    return area_circulo(radio)*altura
#------------------------------------------------------------------------------    
V1=volumen_cilindro(5,10)
print(V1)
print(V1*3)
    