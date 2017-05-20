from turtle import fd, rt, done, speed, ht, lt
def inversa(c):
    r = ''
    for x in c:
        if x == 'I':
            r += 'D'
        else:
            r += 'I'
    return r

def curva(n):
     r = ''
     for i in range(n):
         r = r + 'I' + inversa(r[::-1])
     return r
     
def dragon(n, d):
    fd(d)
    for i in curva(n):
        if i == 'I':
            lt(90)
        else:
            rt(90)
        fd(d)
         
def main():
    speed(99999)
    ht()    
    dragon(25, 1)
    done()
main()