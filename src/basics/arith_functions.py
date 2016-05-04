from math import sqrt
import math
import cmath
# uses arithmetic built in functions

a = 2
b = 4

print pow(a, b)

c = -3

print pow(-a,c)

print abs(pow(-a, c))

f1 = 2.4
f2 = 3.2

result = pow(f1,f2)

print "rounding ", result , round(result)

print "rounding by two decimal points", result , round(result,2)

print "using floor ", result , math.floor(result)

print "using ceil ", result , math.ceil(result)

print "using builtin functions:  sqrt of 123 = " , sqrt(123)

# complex math

#print sqrt(-2)
print cmath.sqrt(-2)

x = 3 + 2j

print "adding complex numbers: ", x+cmath.sqrt(-1)