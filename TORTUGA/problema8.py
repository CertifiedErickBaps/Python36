#Práctica 1: Gráficas de tortuga
# Fecha: 24-Ago-2016
# Autor:   A01379896 Erick Bautista Pérez
#           A01378568 Leonardo Valencia Benitez
#-------------------------------------------------------------------------------

from turtle import fd, lt, done, rt

def escalera(lado):
    for i in range(10):    
        lt(90)
        fd(lado)
        rt(90)
        fd(lado)

def figura_8(lado, lado_largo):
    escalera(lado)
    rt(90)
    fd(lado_largo)
    rt(90)
    fd(lado_largo)
    rt(90)
    fd(lado)

figura_8(20, 200)
done()    
    