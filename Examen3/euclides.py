#Erick Bautista Perez
def euclides(a, b):   
    while b > 0:
        t = b
        b = a % b
        a = t
    return a
def main():
    print(euclides(128, 48))
    print(euclides(25, 35))
    print(euclides(666, 150))
    print(euclides(10, 10))
main()

