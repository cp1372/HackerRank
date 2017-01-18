#!/bin/python
import sys

n = int(raw_input().strip())

for x in xrange(n-1, -1, -1):
    base = ''
    for y in xrange(0, n):
        if y < x:
            base += ' '
        else:
            base += '#'
        
    print base
