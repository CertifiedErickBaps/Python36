# ejercicio de dibujar un cuadro. 
#Erick Bautista Perez, A01379896

from turtle import fd, rt, done

def cuadro(lado):
    for i in range(4):#Es un ciclo repetitivo para no escribir el codigo varias veces (4) es el numero de veces
        print(i, lado) #Se imprime se vera en la pantalla de la derecha
        fd(lado) #Hay que poner la intruccion y los codigos poniendo unos 4 espacios mas para que inicie el codigo
        rt(90)
    
 
    
cuadro(100)
cuadro(50)
done()