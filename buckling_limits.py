'''
@author:borisenglebert, tblaha
@description: This file will contain the limit loads for each component after which a certain type of buckling will occur.
'''
import numpy as np
from math import *
from design import *
from mechanics import *

def interrivet(design,load):
    a=0.9
    c=2.1
    Es = mat[design[0]][3]
    ts = sheets[design[1]]          # [m] thickness of the sheet
    sig = load/(ts*l_tot)
    pitch=ts * sqrt ((a*c*Es)/sig)
    return pitch





