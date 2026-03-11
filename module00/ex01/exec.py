#!/bin/python
import sys

args = sys.argv[1::]

for i in args[len(args)::-1]:
	print(i[::-1].swapcase(), end = ' ')
