#Práctica 1: Gráficas de tortuga
# Fecha: 24-Ago-2016
# Autor:   A01379896 Erick Bautista Pérez
#-------------------------------------------------------------------------------

from turtle import rt, lt, fd, done

def cruz(lado):
    for i in range(4):    
        fd(lado)
        lt(90)
        fd(lado)
        rt(90)
        fd(lado)
        rt(90)
    
    
cruz(100)
done()