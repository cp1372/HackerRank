#!/bin/python
import sys

s = raw_input().strip()
words = 1

for x in s:
    #Comparison on ASCII values
    if x < 'a':
        words += 1
        
print words