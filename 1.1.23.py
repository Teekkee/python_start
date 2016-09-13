#!/usr/bin/python

for a in range(0, 2):
	for b in range(0, 2):
		for c in range(0, 2):
			res = (a or (b and c)) == ((a or b) and (a or not(not c)))
			print(a,b,c,res)