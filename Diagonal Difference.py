#!/bin/python
import sys

n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int, raw_input().strip().split(' ') )
    a.append(a_temp)

primaryDiagonal = 0
secondaryDiagonal = 0

for x in xrange(0,n,1):
    primaryDiagonal += a[x][x]
    secondaryDiagonal += a[x][n-x-1]
 
difference = abs(primaryDiagonal-secondaryDiagonal)
print difference