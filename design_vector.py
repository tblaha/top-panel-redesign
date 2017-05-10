'''
@author: tblaha
Here is the definition of the design vector
'''

#materialtype ['name','yield','ult','Emod','rho']
materialtype=[['steel',1100e6,1275e6,210e9,7.8e3],['aluminium',345e6,483e6,72.4e9,2.78e3]]

#sheets[thicknesses]
sheets=[0.8,1.0,1.2]

#profile
profiles=[[
    [15.,15.,1.5],
    [15.,15.,2.]
          ],
          [
    [15.,15.,1.],
    [15.,15.,1.5],
    [20.,20.,1.5],
    [20.,20.,2.]
          ]]

#design=[#ofstringer, symmetric spacing from either side, sheet material, sheet thickness, [[profile 1 material,profile 1 type],[profile 2 material,profile 2 type]] ]
design=[]
