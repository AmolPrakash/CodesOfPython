import math


#input
x= float(input(" please give number: "))

#estimate
estimate= 1.0
tolerance= .00001

while True:
    estimate= (estimate+ x/estimate)/2
    diff=abs(x- estimate**2)
    if diff<=tolerance:
        break

#printing
print (" the program shows", estimate)
print ("the python built in shows", math.sqrt(x))
