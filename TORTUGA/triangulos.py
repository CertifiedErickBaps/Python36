#Examen 1: Gráficas de tortuga
# Fecha: 22-Ago-2016
# Autor:   A01379896 Erick Bautista Pérez
#-------------------------------------------------------------------------------

from turtle import lt, fd, rt, done

def triangulo(lado):
    for i in range(3):
        fd(lado)
        rt(120)
def triangulo_1(lado):
    triangulo(lado)
    lt(60)
    fd(lado)
    rt(120)    
    fd(lado)
    fd(lado)
    rt(120)
    fd(lado)
    fd(lado)
    rt(120)
    fd(lado)    

triangulo_1(100)
done()