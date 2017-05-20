# Authors: 
#           A01379896 Erick Bautista Pérez
#(This is problem 13.6 from [JOHNSON]) Write a program called encode.py. Define in this program a function 
#called encode(msg) that returns a string containing the ASCII codes of each character in msg separated by spaces. 
#For example, encode("ABC") should return the string "65 66 67".

# October 14, 2016.
def encode(msg):
    resultado = "" #la cadena saldra vacia    
    for c in msg:
        resultado += str(ord(c)) + " "  #Las comillas son un espacio
    return resultado

def main():
    print(encode("ABC"))
    print(encode(""))
    print(encode("Hello World!"))
    print(encode("Programming is fun!"))
    print(encode("THE END"))
    
main()
        
