'''
@author:borisenglebert, tblaha
@description: This file will contain the limit loads for each component after which a certain type of buckling will occur.
'''
import numpy as np
from math import *
from constants import *
from mechanics import *

def interrivet(design,load):
    a=0.9
    c=2.1
    Es = mat[design[0]][3]
    ts = sheets[design[1]]          # [m] thickness of the sheet
    sig = load/(ts*l_tot)
    pitch=ts * sqrt ((a*c*Es)/sig)
    return pitch

def column(design):
    mois=moi(design)
    columncr=[]
    i=0
    for stringer in design[2]: # for every stringer present in the current design
        if stringer < 2: # steel
            E=mat[0][3] # emod
        else:            # al
            E=mat[1][3] # emod
        columncr.append((pi**2)*E*mois[i]/(H*H)) # FACTOR?
        i += 1
    return columncr


# Calculating compression buckling force  
#   needed:
# design vector to obtain thickness, stiffness and stringer pitch
def compbuck(design):
    Kc = 3.6 ## assumed constant
    
    E=mat[design[0]][3]
    t=sheets[design[1]]
    b=l_tot/(len(design[2])-1) ## avg spacing between stringers
    
    
    stress = Kc * E * ((t/b)**2) ## assumed uniform over width
    
    Fcb = stress * (t * l_tot)   #l_tot is width
    return Fcb
