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
    rows.append([1,0,0,-G*H*t_s]                                      + nos*[0]) # Moment contribution by sheet being in shear
    rows.append([0,1,-E*t_s*l_tot/(H),-E*t_s*l_tot*l_tot/(H)] + nos*[0]) # Moment contribution by sheet being in compression
    rows.append([1,1,0,0]                                                     + nos*[1]) # Sum of Forces
    rows.append([l_tot,l_tot/2,0,0])
    for c in design[3]:
        rows[3] += [l_i[c]]                                                               # Sum of moments]

    for d in range(nos):
        rows.append([0,0])

    for e in range(nos):
        if design[2][e] < 2:
            E_i=mat[0][3]
        else:
            E_i=mat[1][3]
        L_i=H
        A_i=profiles[design[2][e]][0]*2*profiles[design[2][e]][2]
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

def weight():
    G   = mat[design[0]] [5]         # [Pa] Shear Mod of the sheet
    E   = mat[design[0]] [3]
    t_s = sheets[design[1]]          # [m] thickness of the sheet

    A_s = t_s * l_tot
    M_s = A_s * H * mat[design[0]][4]

    M_str=0
    for a in design[2]:
        L_str = H
        if a < 2:
            rho = mat[0][4]
        else:
            rho = mat[1][4]
        A_str=profiles[a][0]*2*profiles[a][2]
        M_str += A_str*rho*L_str

    return M_str+M_s




