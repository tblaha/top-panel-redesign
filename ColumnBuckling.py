from Mechanics import*
from math import*
from design import*


#Program finds critical buckling force that can be carried for different stringer geometries and materials

Es = 200.e6
Ea = 72.4e6
L = 0.5
c = 4.

Fsteel = [] ##Tables give buckling loads(N) that correspond to the index of the MoI tables for each material
Fal = []    ##Buckling load for one stringer!




for i in range(len(moi(lst))):
    Fsteel.append(((pi^2)*Es*moi[i])/L^2)
    Fal.append(((pi^2)*Ea*moi[i])/L^2)


print Fsteel
print Fal

        
