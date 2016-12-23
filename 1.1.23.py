#!/usr/bin/python
"""expr
	function update
					"""
					
print("(a or (b and c)) == ((a or b) and (a or not(not c)))")

def func_lul():
	for a in range(0, 2):
		for b in range(0, 2):
			for c in range(0, 2):
				global res
				res = (a or (b and c)) == ((a or b) and (a or not(not c)))
				#print(a,b,c,res)
				return res
def out():
	print(func_lul())

out()

assert res == False, "Keepo"