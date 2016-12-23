#!/usr/bin/python
# v.1.05 - last update(final)

a = raw_input('Factorial from number : ')
def factorial(a):
	try:
		a = int(a)
	except (ValueError, TypeError, NameError) as e:
		print("Error start :", e)
		quit(1)
 	else:
		if a == 1:
			return 1
		elif a == 0:
			return 0
		elif a > 997 or a < 0:
			raise Exception("Attention - TOO DEEP")
		else:
			return a * factorial(a-1)
	out()

def out():
	print'{}{} {}'.format(a , "! = ", factorial(a))

out()

##########################################################
######################Salvation?##########################
##########################################################
#assert factorial([1,2]) == ValueError or TypeError, "Damn"