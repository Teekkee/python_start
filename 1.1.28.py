#!/usr/bin/python
"""expr
	function update
					"""
					
print("(a,c,(not(a or not c and a) == (not(a or not c or c))))")

def funct_LUL():
	for a in range(0, 2):
		for c in range(0, 2):
			global res
			res = (not(a or not c and a) == (not(a or not c or c)))
			return res

def out():
	print(funct_LUL())

out()

assert res == True, "Kappa"