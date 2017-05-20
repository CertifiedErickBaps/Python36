#Práctica 1: Gráficas de tortuga
# Fecha: 24-Ago-2016
# Autor:   A01379896 Erick Bautista Pérez
#           A01378568 Leonardo Valencia Benitez
#-------------------------------------------------------------------------------


from turtle import fd, lt, done
    
def pentagono(lado, veces):
    for i in range(veces):    
        fd(lado)
        lt(72)
        fd(lado)
    
    
    
    

pentagono(100, 5)
done()