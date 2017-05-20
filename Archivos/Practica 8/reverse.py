# Authors: 
#          A01379896 Erick Bautista Perez
#
#Write a program called reverse.py. Define in this program a function called reverse(infile, outfile) 
#that takes two arguments: a string with the name of the input file infile and a string with the name 
#of the output file outfile. The function should write in outfile each of the lines contained in infile 
#but in reversed order. The function should return nothing.
#
# November 4, 2016.

def reverse(infile, outfile):
    with open(infile) as f1:
        s = f1.readlines()
    s.reverse()
    with open(outfile, 'w') as f2:
        for c in s:
            f2.write(c)
        
def main():
    reverse('speak.txt', 'speak_reverse.txt')
main()