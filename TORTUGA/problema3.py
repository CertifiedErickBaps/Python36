#Práctica 1: Gráficas de tortuga
# Fecha: 24-Ago-2016
# Autor:   A01379896 Erick Bautista Pérez
#           A01378568 Leonardo Valencia Benitez
#-------------------------------------------------------------------------------



from turtle import fd, lt, done, home, rt

def triangulo(lado):
    for i in range(4):    
        fd(lado)
        lt(120)
        fd(lado)
        lt(120)
        fd(lado)




def figura(lado):    
    triangulo(lado)
    for i in range(2):    
        fd(lado)
        rt(120)
        fd(lado)
        home()
        lt(60)
        fd(lado)
        lt(120)
        fd(lado)
        home()
        
    
figura(100)
done()    
    