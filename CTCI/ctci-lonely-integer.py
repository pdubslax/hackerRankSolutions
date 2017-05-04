#!/bin/python

import sys

def lonely_integer(a):
	running = 0
	for number in a:
		running ^= number
	return running

    

# n = int(raw_input().strip())
# a = map(int,raw_input().strip().split(' '))
a = [0,0,1,2,1]
print lonely_integer(a)