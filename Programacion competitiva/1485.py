# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 16:40:49 2017

@author: Erick
"""

#You are given a word C of 1000 characters at most, and you must order its characters ascending. 
#In other words, you must find a permutation of its characters, which is lexicographically less than all.

from __future__ import print_function
from __future__ import division

from sys import stdin

entrada = list(stdin.read().strip()) #Borra todo lo blanco de la izquierda y derecha
entrada.sort()
print(''.join(entrada))
#Otra alternativa 
# for c in entrada:
#print(c, end='')
#print()              

print(entrada)
