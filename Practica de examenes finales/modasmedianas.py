# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 09:30:16 2016

@author: Erick
"""

l = [ 1, 10, 4, 2, 4, 3, 3, 1, 1, 3]                                                     
                                                                                         
print(l)                                                                                  
                                                                                         
promedio = sum(l)/len(l)                                                                 
print ("largo ",len(l), ", promedio:",promedio)                                            
                                                                                         
# moda                                                                                   
repeticiones = 0                                                                         
for i in l:                                                                              
    apariciones = l.count(i)                                                             
    if apariciones > repeticiones:                                                       
        repeticiones = apariciones                                                       
                                                                                         
modas = []                                                                               
for i in l:                                                                              
    apariciones = l.count(i)                                                             
    if apariciones == repeticiones and i not in modas:                                   
        modas.append(i)                                                                  
                                                                                         
print ("moda:", modas)                                                                     
                                                                                         
# mediana                                                                                
l.sort()                                                                                 
print (l)                                                                                  
                                                                                         
if len(l) % 2 == 0:                                                                      
    n = len(l)                                                                           
    mediana = (l[n // 2-1] + l[ n// 2] ) /2                                                      
else:                                                                                    
    mediana =l[len(l)/2]                                                                 
                                                                                         
print ('mediana:',mediana) 

# calcular de mediana
# calcular de la media aritmetica
# calcular la moda

#print ("Datos a tratar: ")
#data=[1,4,6,7,2,3,4,7,1,2,4,3,4,5,
#      6,5,2,3,1,2,5,6,7,3,4,1,5,7,
#      1,7,6,5,3,4,3,4,5,5,5,6,7,3,
#      4,5,3,4,5,4,5,6,3,4,3,4,5,3,
#      4,5,3,4,5,3,4,5,3,4,5,3,1,3,
#      4,5,3,4,5,6,5,4,6,5,6,5,1,7]
#
#print (data)
#dOrder=sorted(data)
#
#n=len(dOrder)
#middle= n//2
#
## codigo para calcular la mediana
#if n%2==0:
#    mediana = (dOrder[middle+1] + dOrder[middle+2]) // 2
#else:
#	mediana=dOrder[middle+1]*1
#
#print ('')
#print ('Total datos', n)
#print ('Mediana: ', mediana)
#
## codigo para calcular la media aritmetica
#print ('Mediana Aritmetica: ', round(sum(data)*1/n,2))
#
## codigo para calcular la moda
#repetir = 0                                                                         
#for i in data:                                                                              
#    aparece = data.count(i)                                                             
#    if aparece > repetir:                                                       
#        repetir = aparece                                                       
#                                                                                         
#moda = []                                                                               
#for i in data:                                                                              
#    aparece = data.count(i)                                                             
#    if aparece == repetir and i not in moda:                                   
#        moda.append(i)                                                                  
#                                                                                         
#print ("moda:", moda)