'''
@author:tblaha
'''
from mechanics import *
from design import *
from buckling_limits import *

######################
# Start stuff
######################


for i in range(0,1):
    design= [1,              0,               [ 0,0,0,0 ],                          [ 0,4,8,12 ] ] ## This design vector will later be iterated
    allowable=[5000,5000,5000,5000,500]
    weight(design)
    interrivet(design,15000.)
    failed=[]
    F=0
    buckling=0
    while F < 32000:
        loads=loadpercomponent(design,F,failed)
        if isinstance(loads,int): #if the mechanics function returned 0 (an integer) instead of a list, the matrix is singular --> all components failed.
            break
        if loads[-3]>allowable[-1] and not -1 in failed:
            failed.append(-1)
            F = 0
        for a in range(len(design[2])):
            if loads[a]>allowable[a] and not a in failed:
                failed.append(a)
                F = 0
                break
        F += 100


#design= [1,              0,               [ 0,0,1,0,2 ],                          [ 0,4,6,8,12 ] ]
#print moi(design)







