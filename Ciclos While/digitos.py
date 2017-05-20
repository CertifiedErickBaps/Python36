def digitos(n):
    while n != 0:
        r = n % 10
        n //= 10
        print(r)
        
def main():
    digitos(354)
    print()
    digitos(1000)
    print()
    digitos(7)
    print()
    digitos(123456789)
    print()
    
    
main()