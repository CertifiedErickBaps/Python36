#Erick Bautista Perez A01379896

def vocales(archivo_entrada):
    with open(archivo_entrada) as f:
        f = f.read()
        w = f.split()
        a = 'aeiouAEIOU'
        b = 0
        for c in w:
            if c[0] in a:           
                b += 1
        return b
            
    
def main():
    print(vocales('entrada1.txt'))
    print(vocales('entrada2.txt'))
main()