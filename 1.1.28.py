#!/usr/bin/python

for a in range(0, 2):
	for c in range(0, 2):
		print(a,c,(not(a or not c and a) == (not(a or not c or c))))