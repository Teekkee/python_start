#!/usr/bin/python
# v.1.01

a = raw_input('Factorial from number : ')
def factorial(a):
	try:
		a = int(a)
	except ValueError as e:
		print("Hard to catch: ", e)
 	else: 
		if a == 1:
			return 1
		else:
			return a * factorial(a-1)

def out():
	print'{}{} {}'.format(a , "! = ", factorial(a))

out()