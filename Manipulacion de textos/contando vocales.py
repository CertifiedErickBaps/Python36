# contando vocales
def cuenta_vocales(cadena): #queremos devolver cuantas vocales hay en esta cadena
    s = 0 #esto se pone fuera del for para sumar las vocales    
    for c in cadena:
        if c in "aeiouAEIOU":
            s += 1
    return s #el return va alineado con el for
        
def main():
    print(cuenta_vocales("Hola mundo"))
    print(cuenta_vocales("El leo :v"))
    print(cuenta_vocales("xyz"))
    print(cuenta_vocales(""))
    print(cuenta_vocales("Adios"))
main()
