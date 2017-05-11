'''
@author: tblaha
@description: In here the mechanics function are defined that can be used in the main program to find the loads carried by each individual component and the overall displacement etc.
              A precise description of the solution vector is yet to come
              This requires the design.py script with all the definitions!
'''
import numpy as np
from design import *

def loadpercomponent(load):
    G   = mat[design[0]] [5]         # [Pa] Shear Mod of the sheet
    E   = mat[design[0]] [3]
    t_s = sheets[design[1]]          # [m] thickness of the sheet
    rows=[]
    rows.append([1,0,0,-G*H*l_tot*l_tot]                                      + nos*[0]) # Moment contribution by sheet being in shear
    rows.append([0,1,-E*t_s*l_tot*l_tot/(2*H),-E*t_s*l_tot*l_tot*l_tot/(3*H)] + nos*[0]) # Moment contribution by sheet being in compression
    rows.append([0,0,0,0]                                                     + nos*[1]) # Sum of Forces
    rows.append([0,0,0,0])
    for c in design[3]:
        rows[3] += [l_i[c]]                                                               # Sum of moments]

    for d in range(nos):
        rows.append([0,0])

    for e in range(nos):
        E_i=mat[design[2][e]] [3]
        L_i=H
        A_i=profiles[design[2][e]][0]*profiles[design[2][e]][1]
        rows[4+e] += [-E_i*A_i/L_i]
        rows[4+e] += [-E_i*A_i*(l_i[design[3][e]])/L_i]
        for f in range(e):
            rows[4+e] += [0]
        rows[4+e] += [1]
        for g in range(nos-e-1):
            rows[4+e] += [0]

    matrix = np.array(rows)

    augmented=[]
    for h in range(2):
        augmented += [0]
    augmented += [load]
    augmented += [load*l_tot/2]
    for i in range(nos):
        augmented += [0]

    solution = np.linalg.solve(matrix,augmented)
    return solution
