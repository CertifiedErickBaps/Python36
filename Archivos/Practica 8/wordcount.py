# Authors: 
#          A01379896 Erick Bautista Perez
#
#Write a program called wordcount.py. Define in this program a function called wordcount(infile) 
#that takes a string with the name of an input file infile and returns the number of lines, number 
#of words, and number of characters in the ﬁle.
#To test your program, create a file called crocodile.txt with the following content:
#
# November 4, 2016.
def words(w):    
    with open('crocodile.txt') as f:
        c = 0        
        for z in f.readlines():
            c += len(z.split())
    return c
def lineas(l):
    with open('crocodile.txt') as f:
        c = 0        
        for z in f.readlines():
            if z != None:
                c += 1
        return c    
            
def characters(c):
    with open('crocodile.txt') as f:
        c = 0
        for z in f.readlines():
            if z != None:
                c += len(z)
        return c    

def wordcount(infile):
    a = words(infile)
    b = lineas(infile)
    c = characters(infile)
    return b, a, c        
        
def main():
     print(wordcount('crocodile.txt'))     
main()

#def wordcount(infile):
#    l = 0
#    c = 0
#    w = 0
#    with open(infile) as f:    
#        for z in f:
#            l += 1
#            c += len(z)
#            w += len(z.split())
#    return l, c, w
