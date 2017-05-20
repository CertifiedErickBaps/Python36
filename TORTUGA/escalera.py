#Dibujando una escalera con cuadros
from turtle import rt, fd, done, lt
def cuadro(lado):
    for i in range(4):
        fd(lado)
        lt(90)
def escalera(lado, veces):
    for i in range(veces):    
        cuadro(lado)
        fd(lado)
        lt(90)
        fd(lado)
        rt(90)
        
    
    
    
    
    
    
escalera(50, 5)
done()    
    