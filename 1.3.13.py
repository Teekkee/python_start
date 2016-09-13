#!/usr/bin/python

fib = [0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181,6765,10946]
tog = sum(fib)
cutted = len(fib)/2			#Checking length to cut
cutting = fib[:-cutted]		#Cutting into new one
neg = sum(cutting[1::2])	#Summary of negative elements
print(tog) 					#Whole list
print(neg) 					#Negative ones
print(tog + neg) 			#Summary