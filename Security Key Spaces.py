import sys

message = str(raw_input())
shift = int(raw_input())
cipher = ''


for n in message:
    x = ( int(n)+shift ) % 10
    cipher += str(x)
    
print cipher