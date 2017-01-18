#!/bin/python

import sys

alice = raw_input().strip().split(' ')
bob = raw_input().strip().split(' ')

alice_score, bob_score = 0, 0

for x in xrange(0,3,1):
    if int(alice[x]) > int(bob[x]):
        alice_score += 1
    if int(alice[x]) < int(bob[x]):
        bob_score += 1
        
print alice_score, bob_score