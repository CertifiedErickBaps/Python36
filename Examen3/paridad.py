#Erick Bautista Perez A01379896
def cuenta_vocales(cadena): #queremos devolver cuantas vocales hay en esta cadena
    s = 0 #esto se pone fuera del for para sumar las vocales    
    for c in cadena:
        if c in "1": #o puedes poner == "1"
            s += 1
    return s #el return va alineado con el for

def paridad(bits):
    n = cuenta_vocales(bits)
    if n % 2 == 0:
        return bits + "0"
    else:
        return bits + "1"
def main():
    print(paridad("1000110"))
    print(paridad("1011001"))
    print(paridad("0000000"))
    print(paridad("1111111"))
    print(paridad("0010000"))
    print(paridad("1101111"))
main()