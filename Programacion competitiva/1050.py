# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division

from sys import stdin
from fractions import gcd

N = int(stdin.read())

print(N)

c = 0
for x in range(1, N + 1):
    if gcd(N, x) == 1:
        c += 1
print(c)