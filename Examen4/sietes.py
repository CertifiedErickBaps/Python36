#Erick Bautista Perez A01379896    
def siete(n):
    s = []
    for c in range(1, n):
        if c % 10 == 0:
            a = c + 7
            s.append(a)
    return s
        

def sietes(n):
    s = []
    for c in range(1, n + 1):        
        if c % 7 == 0:            
            s.append(c)
        elif c in siete(n):
            s.append(c)
        
    return s
        
            
    
def main():
    print(sietes(20))
    print(sietes(50))
    print(sietes(87))
    print(sietes(6))
main()
