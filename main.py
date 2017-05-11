'''
@author:tblaha
'''
from mechanics import *
from design import *
from buckling_limits import *
import itertools

######################
# Design Vector
######################
#design=[sheet material, sheet thickness, [stringer 1 type,stringer 2 type...], [stringer 1 position, stringer 2 position...]]
design= [1,              1,               [ 0,0,0,0 ],                          [ 0,3,6,9 ] ]


######################
# Combinatorics
######################
#positions=[[0,6,12],[0,4,8,12],[0,3,6,9,12],[0,3,5,7,9,12],[0,2,4,6,8,10,12],[0,1,3,5,7,9,11,12]]
#for a in range(len(mat)):
    #for b in range(len(sheets)):
        #c=1

#def getAllCombinations(object_list):
    #uniq_objs = set(object_list)
    #combinations = []
    #for obj in uniq_objs:
        #for i in range(0,len(combinations)):
            #combinations.append(combinations[i].union([obj]))
        #combinations.append(set([obj]))
    #return combinations

#combinations=getAllCombinations(range(0,12))
#print list(combinations)

######################
# Start stuff
######################


for i in range(0,1):
    design= [1,              1,               [ 0,0,0,0 ],                          [ 0,4,8,12 ] ]
    allowable=[1500,1500,1500,1500,1000]
    weight(design)
    moi(design,1)
    interrivet(design,15000.)
    failed=[]
    F=0
    while F < 32000:
        loads=loadpercomponent(design,F,failed)
        if isinstance(loads,int):
            break
        if loads[-3]>allowable[-1] and not -1 in failed:
            print 'sheet failure at', F
            #print loads
            failed.append(-1)
            F = 0
        for a in range(len(design[2])):
            if loads[a]>allowable[a] and not a in failed:
                print a,'stringer failure at', F
                #print loads
                failed.append(a)
                F = 0
                break
        #print failed
        F += 100








