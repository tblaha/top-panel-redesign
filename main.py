'''
@author:tblaha
'''
from mechanics import *
from design import *
from buckling_limits import *

######################
# Design Vector
######################
#design=[sheet material, sheet thickness, [stringer 1 type,stringer 2 type...], [stringer 1 position, stringer 2 position...]]
design= [1,              1,               [ 0,0,0,0 ],                          [ 0,3,6,9 ] ]


######################
# Start stuff
######################

weight(design)
moi(design,b)
print interrivet(design,15000)
loadpercomponent(design,a*50)
