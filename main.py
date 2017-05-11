'''
@author:tblaha
'''
#from __future__ import print_function
from mechanics import *
from constants import *
from buckling_limits import *
from Combinations import *

######################
# Start stuff
######################

def progfail(design):
    sheetbuckling=9600 ##will be changed to proper value later
    allowable=column(design) + [sheetbuckling]
    
    weigth=weight(design)
    ir=interrivet(design,15000.)
    failed=[]
    F=0
    buckling=False
    failure = 0
    while F < 32000:
        loads=loadpercomponent(design,F,failed)
        failure=max(failure,F)
        if isinstance(loads,int): #if the mechanics function returned 0 (an integer) instead of a list, the matrix is singular --> all components failed.
            break
        if loads[-3]>allowable[-1] and not -1 in failed:
            failed.append(-1)
            if buckling == False:
                buckling = F
            F = 0
        for a in range(len(design[2])):
            if loads[a]>allowable[a] and not a in failed:
                failed.append(a)
                if buckling == False:
                    buckling = F
                F = 0
                break
        F += 100
    
    if buckling > 14000:
        with open('MDO.txt','a') as f:
            f.write('{0},{1},{2},{3} | {4},{5},{6},{7}\n'.format(design[0],design[1],design[2],design[3],buckling,failure,weigth,ir))



for a in range(len(mat)):
    for b in range(len(sheets)):
        for c in range(3,9):
            for d in stringersamount(ceil(float(c)/2)):
                if c%2 == 0:
                    helper=d+d[::-1]
                else:
                    helper = d+d[-2::-1]
                design=[a,b,helper,strpitch[c-2]]              # such that 3 stringer give the element no1 of that list.
                progfail(design)











