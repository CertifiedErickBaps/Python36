#@author: Erick Bautista Perez A01379896

def fizzbuzz(n):
    lista = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            lista.append('FizzBuzz')
        elif i % 3 == 0:
            lista.append('Fizz')
        elif i % 5 == 0:
            lista.append('Buzz')
        else:
            lista.append(str(i))
    return lista
    
def main():
    print(fizzbuzz(1))
    print(fizzbuzz(5))
    print(fizzbuzz(15))
    print(fizzbuzz(60))
main()