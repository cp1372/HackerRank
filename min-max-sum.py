#!/bin/python
import sys

numbers = raw_input().strip().split(' ')
numbers = map(int, numbers)
numbers.sort()

minSum, maxSum = 0, 0
n = len(numbers)
for x in range(0, n-1):
    minSum += numbers[x]
    maxSum += numbers[n-1-x] 
    
print minSum, maxSum