#Dibujando la figura 10

from turtle import fd, lt, done, rt


def estrella(lado):
    for i in range(5):    
        lt(72)
        fd(lado)
        rt(144)
        fd(lado)
    
    
estrella(100)
done()