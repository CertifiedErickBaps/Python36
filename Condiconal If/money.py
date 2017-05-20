def main():

    c = int(input("Total cents: "))
    u = c // 100
    r = c % 100 #Ahora r tiene asignado un valor
    q = r // 25
    r %= 25 #Ahora r tiene otro valor asignado
    d = r // 10
    r %= 10
    n = r // 5
    r %= 5
    p = r % 5
    print("Dollars =", u)
    print("Quarters =", q)
    print("Dimes =", d)
    print("Nickles =", n)
    print("Pennies =", p)
main()