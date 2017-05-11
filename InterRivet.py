import math
from math import sqrt
print'Enter inter rivet buckling stress in Pa'

sig = float(input('Enter value of inter rivet buckling stress:'))

#----------------------MAIN PROGRAM-------------------

#Tables gives rivet spacing for steel and aluminium for given thicknesses in lists


steel= []
aluminium= []
a=0.9
c=2.1
Es = 210.e6
Ea = 72.4e6
#sheets[thicknesses m]
sheets=[0.0008,0.001,0.0012]

for i in range(len(sheets)):
    steel.append(sheets[i]*sqrt((a*c*Es)/sig))
    aluminium.append(sheets[i]*sqrt((a*c*Ea)/sig))

print steel
print aluminium
