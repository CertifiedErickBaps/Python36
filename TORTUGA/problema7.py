#Práctica 1: Gráficas de tortuga
# Fecha: 24-Ago-2016
# Autor:   A01379896 Erick Bautista Pérez
#           A01378568 Leonardo Valencia Benitez
#-------------------------------------------------------------------------------

from turtle import fd, lt, done, home, rt

def repeticion(lado, pequeño):
    for i in range(10):
        lt(90)
        fd(lado)
        rt(90)
        fd(pequeño)
        rt(90)
        fd(lado)
        lt(90)
        fd(pequeño)
def figura_7(lado, pequeño, largo):
    repeticion(lado, pequeño)
    rt(90)
    fd(pequeño)
    rt(90)
    fd(largo)
    rt(90)
    home()
     


figura_7(100, 20, 400)
done()    
    