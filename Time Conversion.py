#!/bin/python
#Messy solution

import sys
time = raw_input().strip('')

converted = ''
a = str(int(time[0]))
b = str(int(time[1]))

if time.__contains__("AM"):
    if a == '1' and b == '2':
        a, b = '0','0'
        
if time.__contains__("PM") and not (a == '1' and b == '2'):
    a = str(int(time[0])+1)
    b = str(int(time[1])+2)
    if a == '2' and b == '4':
        a, b = '0','0'
        
converted += a
converted += b

converted += time[2:len(time)-2]
    
print converted