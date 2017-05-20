#Práctica 1: Gráficas de tortuga
# Fecha: 24-Ago-2016
# Autor:   A01379896 Erick Bautista Pérez
#           A01378568 Leonardo Valencia Benitez
#-------------------------------------------------------------------------------



from turtle import lt, fd, done, rt

def cuadro(lado):
    for i in range(4):    
        fd(lado)
        rt(90)
        

def figura (lado):
    cuadro(lado)
    for i in range(4):            
        lt(60)
        fd(lado)
        rt(120)
        fd(lado)
        rt(30)
        
    
figura(100)
done()