#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May 12 00:35:17 2017

@author: PereiraJoao
"""
from collections import OrderedDict

comb = []
lst = [1,2,3,4,5,6] # List of data which combinations are to be calculated for
NS = input("Enter the range for the combinations: (2-4) ")# I.E Number of stringers 
count = NS

if NS == 4:
    for j in range (6):
        for i in range (6):
            for k in range (6):
                for s in range (6):
                    opt = [lst[j],lst[i],lst[k],lst[s]]
                    comb.append(opt)
elif NS ==3:
    for j in range (6):
        for i in range (6):
            for k in range (6):
                opt = [lst[j],lst[i],lst[k]]
                comb.append(opt)
    
elif NS == 2:
    for j in range (6):
        for i in range(6):
            opt = [lst[j],lst[i]]
            comb.append(opt) 
            
comb1 = map(list, OrderedDict.fromkeys(map(tuple,comb)))

print comb1
print "Number of possible combinations: ",len(comb1)