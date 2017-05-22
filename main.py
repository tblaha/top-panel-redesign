'''
@author:tblaha
'''
#from __future__ import print_function
from mechanics import *
from constants import *
from combinations import *

######################
# Start stuff
######################

def progfail(design):
    global outfile
    allowable=column(design) + [compbuck(design)]
    
    panelweight=weight(design)
    ir=interrivet(design,15000.)
    failed=[]
    sequence=[]
    
    i=0
    F=0
    bucklingload=False
    failureload = 0
    while F < 100000:
        F += 100
        loads=loadpercomponent(design,F,failed)
        failureload=max(failureload,F)
        if isinstance(loads,int): #if the mechanics function returned 0 (an integer) instead of a list, the matrix is singular --> all components failed.
            break
        
        ############################
        # Grabbing failures and resetting simulation
        ############################
        if loads[-3]>allowable[-1] and not -1 in failed: ## Sheet failure?
            failed.append(-1)
            if bucklingload == False:
                bucklingload = F
            sequence.append([F,-1])
            F = 0
        
        tempfail=[]
        for a in range(len(design[2])): ## Get all stringer failures that would have occured in this iteration
            if loads[a]>allowable[a] and not a in failed: ## Stringer failure?
                tempfail.append(strpitch[len(design[2])-2][a])
                if bucklingload == False:
                    bucklingload = F
                
        ############################
        # processing failures (ie removing the proper element and appending it to the sequence list)
        ############################
        if len(tempfail) and len(tempfail) > 1: ## only let one stringer fail
            meanpos=int(float(sum(tempfail))/len(tempfail)+0.5)
            dev=[]
            for position in tempfail:
                dev.append(abs(meanpos-0.01-position)) ## min 0.01 such that the stringer on the left is removed in case there are more than one stringers at exactly the same distace from the meanpos
            doomedpos = tempfail[dev.index(min(dev))]
            
            failed.append(strpitch[len(design[2])-2].index(doomedpos))
            sequence.append([F,strpitch[len(design[2])-2].index(doomedpos)])
            F = 0
            
        elif len(tempfail):
            failed.append(strpitch[len(design[2])-2].index(tempfail[0]))
            sequence.append([F,strpitch[len(design[2])-2].index(tempfail[0])])
            F = 0
            
    ###########################################
    # when analysis is done and requirements achieved, return the configuration
    ###########################################
    #if bucklingload > 14000 and failureload > 28000 and panelweight < 1:
    return sequence + [design[0],design[1],design[2],design[3]] + [bucklingload,failureload,panelweight,ir]

#outfile = []
#i=0
#for a in range(len(mat)):
##for a in range(1,2):
    #for b in range(len(sheets)):
    ##for b in range(0,1):
        #for c in range(3,9):
        ##for c in range(4,5):
            #for d in stringersamount(ceil(float(c)/2)):
                #if c%2 == 0:
                    #helper=d+d[::-1]
                #else:
                    #helper = d+d[-2::-1]
                #design=[a,b,helper,strpitch[c-2]]              # such that 3 stringer give the element no1 of that list.
                #analysis=progfail(design)
                #if analysis:
                    #outfile.append(analysis)
                #if not i%100:
                    #print '{0}/{1}'.format(i,18576)
                #i += 1

design = [1,0,[5,5,5,5,5,5],strpitch[4]] # orig design
#design = [0,0,[0,0,0],strpitch[1]]
print progfail(design)

#outfile.sort(key=lambda x: x[-2]) # sort by weight
#with open('MDO.txt','a') as f:
#    i=0
#    for line in outfile:
#        f.write(str(line) + '\n')
    
    
    [[20900, -1], [49400, 2], [38500, 0], [18600, 1], [8500, 3], [4000, 4], 1, 0, [5, 5, 5, 5, 5, 5], [0, 3, 5, 7, 9, 12], 20900, 49400, 1.112, 0.04322346029646401]
