# Authors: 
#          A01379896 Erick Bautista Perez
#
#Write a program called linenum.py. Define in this program a function called linenum(infile, outfile) 
#that takes two arguments: a string with the name of the input file infile and a string with the name 
#of the output file outfile. The function should write in outfile each of the lines contained in infile 
#but adding the line number along the left edge. The function should return nothing.
#
# November 4, 2016.
def linenum(infile, outfile):
    s = 1    
    with open(infile) as f1:      
        a = f1.readlines()           
    with open(outfile, 'w') as f2:       
        for c in a:            
            f2.write(str(s) + ': ' + c)                
            s += 1
        

def main():
    linenum('bat.txt', 'bat_linenum.txt')
main()