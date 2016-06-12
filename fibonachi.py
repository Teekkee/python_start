#!/usr/bin/python

def fib(n):
	a, b = 0, 1
	while a < n:
		print(a)
		a, b = b, a+b
	print(' ')
c = float(input('Vvedite chislo n dlya funccii fibonachi: '))
fib(c)
