import math
from math import sqrt
print'Enter value of compression force under which inter-rivet buckling occurs(in Newtons)'
from Mechanics import*
from design import*
import numpy as np
F = float(input('Enter value of compression force:'))

#----------------------MAIN PROGRAM-------------------

#Tables gives rivet spacing for steel and aluminium for given thicknesses in lists

A = []
for i in range(len(sheets)):
    A.append(0.4*sheets[i])

sig = []
for x in range(len(sheets)):
    sig.append(F/A[i])

steel= []
aluminium= []
a=0.9
c=2.1
Es = 210.e6
Ea = 72.4e6


for i in range(len(sheets)):
    steel.append(sheets[i]*sqrt((a*c*Es)/sig[i]))
    aluminium.append(sheets[i]*sqrt((a*c*Ea)/sig[i]))

print steel
print aluminium
