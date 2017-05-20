# Authors: 
#          A01379896 Erick Bautista Pérez
#          A01378568 Leonardo Valencia Benitez
#
#Me permite convertir de byte a kibibyte y despues a mebibyte
#
# August 31, 2016.


a=int(input("Number of bytes: "))
kib = a/1024
mib= kib/1024
print(a, "is equal to" , mib, "MiB.") 
   
