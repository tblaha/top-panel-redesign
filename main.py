'''
@author:tblaha
'''
from mechanics import *
from design import *

for a in range(1000):
    for b in design[2]:
        weight()
        moi(b)
    loadpercomponent(a*50)
