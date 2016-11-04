#!/bin/python
import sys

input = str(raw_input())
output = ''

for n in input:
    x = ( int(n)+1 ) % 10
    output += str(x)
    
print output