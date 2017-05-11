'''
@author: tblaha,dayazyan
@description: In here the mechanics function are defined that can be used in the main program to find the loads carried by each individual component and the overall displacement etc.
              A precise description of the solution vector is yet to come
              This requires the design.py script with all the definitions!
'''
import numpy as np
from math import *
from design import *

def loadpercomponent(design,load,failed=[]):
    nos=len(design[2]) # Number of stringers
    brokensheets=0
    for a in failed:
        if a < 0:
            brokensheets=2

    G   = mat[design[0]] [5]         # [Pa] Shear Mod of the sheet
    E   = mat[design[0]] [3]
    if brokensheets == 2:
        G=0
        E=0

    t_s = sheets[design[1]]          # [m] thickness of the sheet

    matrix = np.zeros((nos+4,nos+4))

    matrix[0]=nos*[0] + [1,0,0,-G*H*t_s]
    matrix[1]=nos*[0] + [0,1,0,-G*t_s*l_tot]
    matrix[2]=nos*[1] + [1,1,0,0]

    helper=[]
    for b in design[3]:
        helper.append(l_i[b])
    matrix[3]= helper + [l_tot,l_tot/2,0,0]
    for c in range(nos):
        A_i=profiles[design[2][c]][0]*2*profiles[design[2][c]][2]
        L_i=H
        if c in failed:
            E_i=0
        elif design[2][c] < 2:
            E_i=mat[0][3]
        else:
            E_i=mat[1][3]
        matrix[4+c][c]=1
        matrix[4+c][6]=-E_i*A_i/L_i
        matrix[4+c][7]=-E_i*A_i*l_i[design[3][c]]/L_i

    augmented=np.zeros(nos+4)
    augmented[2]=load
    augmented[3]=load*l_tot/2
    try:
        solution = np.linalg.solve(matrix,augmented)
        return solution
    except np.linalg.linalg.LinAlgError:
        print "All components have failed at ", load
        return 0


def weight(design):
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


def moi(design):
    lst=[]
    for stringer_id in design[2]:
        a = profiles[stringer_id][0]
        t = profiles[stringer_id][2]
        #Centroid location
        Centr = ((a-t)*t*0.5*t+a*t*0.5*a)/((a-t)*t+a*t)
        I = (1./12.)*(a-t)*(t**3.)+(a-t)*t*((Centr-0.5*t)**2)+ (1./12.)*t*(a**3.)+t*a*((0.5*a-Centr)**2)
        lst.append(I)

    return lst # list containes ONLY moments of inertia

