# Autor:
#          A01379896 Erick Bautista Pérez

def arctanh(x, n):
    s=0 
    for k in range(1, n + 1):
        s += (x ** (2 * k - 1)) / (2 * k - 1)
    return s
    
def main():
    for n in range(5, 41, 5):
        print(n, arctanh(0.5, n))
        
main()