# Dibuja un cuadro.

from turtle import fd, rt, done

def cuadro(lado):
    for i in range(4):
        print(i, lado)
        fd(lado)
        rt(90)
        
def cuatro_cuadros(lado):
    for i in range(4):
        cuadro(lado)
        rt(90)
    
cuatro_cuadros(100)
done()