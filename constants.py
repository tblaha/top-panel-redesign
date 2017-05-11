'''
@author: tblaha
Here is the definition of all design constants, constraints and the design vector that holds the choices
'''
import numpy as np

###################
# Geometry
###################

H     = 0.5                    #[m], height of the panel
l_tot = 0.4                    #[m], width of the panel
l_i = [0.]                     #[m], 13 quantized positions
for a in range(0,11):
    l_i.append((26.79+34.64*a)/1000)
l_i.append(400./1000) # length is 13



###############################
# Material types and profiles
###############################

#materialtype format: ['name','yield','ult','Emod','rho']
mat=[['steel',1100e6,1275e6,210e9,7.8e3],['aluminium',345e6,483e6,72.4e9,2.78e3]]
for b in range(0,2):
    mat[b].append(mat[b][3]/(2*(1+0.3)))

#sheets[thicknesses m]
sheets=[0.0008,0.001,0.0012]

#profile
profiles=[
    [0.015,0.015,0.0015],# St
    [0.015,0.015,0.002],
    [0.015,0.015,0.001], # AL
    [0.015,0.015,0.0015],
    [0.02,0.02,0.0015],
    [0.02,0.02,0.002]
          ]

strpitch=[
    [0,12],         #2
    [0,6,12],         #3
    [0,4,8,12],         #4
    [0,3,6,9,12],         #5
    [0,3,5,7,9,12],         #6
    [0,2,4,6,8,10,12],         #7
    [0,1,3,5,7,9,11,12]          #8
        ]
