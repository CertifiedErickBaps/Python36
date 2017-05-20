#Práctica 1: Gráficas de tortuga
# Fecha: 24-Ago-2016
# Autor:   A01379896 Erick Bautista Pérez
#           A01378568 Leonardo Valencia Benitez
#-------------------------------------------------------------------------------



from turtle import fd, lt, done, rt

def hexagono(lado):
    for i in range(6):
        fd(lado)
        lt(60)
    
    

def figura_4(lado):
    hexagono(lado)    
    fd(lado)
    rt(30)
    
    for i in range(6):
        fd(lado)    
        lt(90)
        fd(lado)
        lt(90)
        fd(lado)        
        rt(120)    
    
    
    
figura_4(100)
done()    
    