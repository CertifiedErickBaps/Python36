
from turtle import rt, fd, done, lt

def escalera(lado): #Aqui la funcion "def" sirve para definir los valores que se encuentran hasta abajo
    for i in range(4): #Numero de veces que se repitira el procedimiento
        fd(lado) #Aqui lado significa "x" numero seleccionado para 
        lt(90)
        fd(lado) #Veces es igual a "x" numero y se puede ver abajo
        rt(90)
        


escalera(50) #Aqui estan los valores establecidos por los valores de def escalera
done()
