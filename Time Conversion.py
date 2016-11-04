#!/bin/python

import sys
time = raw_input().strip('')
converted = ''
a = ''
b = ''
if time.__contains__("PM"):
    a += str(int(time[0])+1)
    b += str(int(time[1])+2)
    if b == '4':
        a, b = '0','0'
        
    converted += a
    converted += b

converted += time[2:len(time)-2]
    
print converted