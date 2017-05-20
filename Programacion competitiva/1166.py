# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 16:10:27 2017

@author: Erick
"""

from __future__ import print_function
from __future__ import division

from sys import stdin

nums = [int(i)for i in stdin.read().split()]
it = iter(nums)

for i in range (next(it)):
    par = 0
    impar = 0
    for j in range(next(it)):
        x = next(it)
        if x % 2 == 0:
            par += 1
        else:
            impar += 1
    print(par, 'even and', impar, 'odd.')
    
#Tarea 1078