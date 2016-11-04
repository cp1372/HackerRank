#!/bin/python
import sys

n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))
pos, neg, zeros = 0.0, 0.0, 0.0


for x in arr:
    if (x > 0(:
        pos +=1
    elif (x < 0):
        neg +=1
    else:
        zeros += 1
        
print (pos/n)
print (neg/n)
print (zeros/n)
