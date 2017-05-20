# Insertando espacios

def inserta_espacios(cadena):
    resultado = "" #la cadena saldra vacia    
    for c in cadena:
        resultado += c + " " #LAs comillas son un espacio
    return resultado[:-1] #Para poder eliminar el ultimo espacio y que no salga

def main():
    print(inserta_espacios("Hola"))
    
main()