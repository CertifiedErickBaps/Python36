nombre = input("Nombre del video: ")
num = int(input("Numero de fotoramas: "))
archivo = open("Paths.txt", "w")
cadena = "["
if num > 10:
	lim = 10
else:
	lim = num
for i in range (0,lim):
	cadena += "'Imagenes/" + nombre + "0" + str(i) + ".gif',"
if num > 10:
	for i in range (10,num):
		cadena += "'Imagenes/" + nombre + str(i) + ".gif',"
cadena = cadena[:-1]
cadena += "]"
archivo.write(cadena+"\n")