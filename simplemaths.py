#!/usr/bin/python

import math
def rib(h,v):
	S = (3*v)/h
	hdig = math.sqrt(math.sqrt(S)**2 + math.sqrt(S)**2)
	rb = math.sqrt(h**2 + hdig**2)
	print(rb)

h = float(input('Vvedite visotu pravilnoi chetirehugolnoi piramidi: '))
v = float(input('Vvedite ob\'em pravilnoi chetirehugolnoi piramidi: '))
rib(h,v)