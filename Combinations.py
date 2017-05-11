#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 11 16:23:40 2017

@author: PereiraJoao
"""
from collections import OrderedDict

comb = []
lst = [1,2,3,4,5,6] # List of data which combinations are to be calculated for
NS = input("Enter the range for the combinations: (2-4) ")# I.E Number of stringers 
count = NS

if NS == 4: # Calculates possibe combinations for 4 stringers (on one symmetrical side)
    
    count = NS   
    while count > 1:
        if count == NS:
            for j in range (5,-1,-1):
                opt = [lst[5],lst[5],lst[5],lst[j]]
                comb.append(opt) 
        if count == NS-1:
            for j in range (5,-1,-1):
                for i in range (5,-1,-1):
                    opt = [lst[5],lst[5],lst[j],lst[i]]
                    comb.append(opt)
        if count == NS-2:
            for j in range (5,-1,-1):
                for i in range (5,-1,-1):
                    for k in range (5,-1,-1):
                        opt = [lst[5],lst[j],lst[i],lst[k]]
                        comb.append(opt)
        count = count -1
        
    count = NS   
    while count > 1:
        if count == NS:
            for j in range (4,-2,-1):
                opt = [lst[4],lst[4],lst[4],lst[j]]
                comb.append(opt) 
        if count == NS-1:
            for j in range (4,-2,-1):
                for i in range (4,-2,-1):
                    opt = [lst[4],lst[4],lst[j],lst[i]]
                    comb.append(opt)
        if count == NS-2:
            for j in range (4,-2,-1):
                for i in range (4,-2,-1):
                    for k in range (4,-2,-1):
                        opt = [lst[4],lst[j],lst[i],lst[k]]
                        comb.append(opt)
        count = count -1  
        
    count = NS   
    while count > 1:
        if count == NS:
            for j in range (3,-3,-1):
                opt = [lst[3],lst[3],lst[3],lst[j]]
                comb.append(opt) 
        if count == NS-1:
            for j in range (3,-3,-1):
                for i in range (3,-3,-1):
                    opt = [lst[3],lst[3],lst[j],lst[i]]
                    comb.append(opt)
        if count == NS-2:
            for j in range (3,-3,-1):
                for i in range (3,-3,-1):
                    for k in range (3,-3,-1):
                        opt = [lst[3],lst[j],lst[i],lst[k]]
                        comb.append(opt)
        count = count -1    

    count = NS   
    while count > 1:
        if count == NS:
            for j in range (2,-4,-1):
                opt = [lst[2],lst[2],lst[2],lst[j]]
                comb.append(opt) 
        if count == NS-1:
            for j in range (2,-4,-1):
                for i in range (2,-4,-1):
                    opt = [lst[2],lst[2],lst[j],lst[i]]
                    comb.append(opt)
        if count == NS-2:
            for j in range (2,-4,-1):
                for i in range (2,-4,-1):
                    for k in range (2,-4,-1):
                        opt = [lst[2],lst[j],lst[i],lst[k]]
                        comb.append(opt)
        count = count -1  

    count = NS   
    while count > 1:
        if count == NS:
            for j in range (1,-5,-1):
                opt = [lst[1],lst[1],lst[1],lst[j]]
                comb.append(opt) 
        if count == NS-1:
            for j in range (1,-5,-1):
                for i in range (1,-5,-1):
                    opt = [lst[1],lst[1],lst[j],lst[i]]
                    comb.append(opt)
        if count == NS-2:
            for j in range (1,-5,-1):
                for i in range (1,-5,-1):
                    for k in range (1,-5,-1):
                        opt = [lst[1],lst[j],lst[i],lst[k]]
                        comb.append(opt)
        count = count -1 
    count = NS        
    while count > 1:
        if count == NS:
            for j in range (0,6,1):
                opt = [lst[0],lst[0],lst[0],lst[j]]
                comb.append(opt) 
        if count == NS-1:
            for j in range (0,6,1):
                for i in range (6):
                    opt = [lst[0],lst[0],lst[j],lst[i]]
                    comb.append(opt)
        if count == NS-2:
            for j in range (0,6,1):
                for i in range (0,6,1):
                    for k in range (0,6,1):
                        opt = [lst[0],lst[j],lst[i],lst[k]]
                        comb.append(opt)
        count = count -1

elif NS == 3: # Calculates combinations for 3 stringers .... 
    
    while count > 0:
        if count == NS:
            for j in range (5,-1,-1):
                opt = [lst[5],lst[5],lst[j]]
                comb.append(opt) 
        if count == NS-1:
            for j in range (5,-1,-1):
                for i in range (5,-1,-1):
                    opt = [lst[5],lst[j],lst[i]]
                    comb.append(opt)       
        count = count -1   
    count = NS   
    while count > 0:
        if count == NS:
            for j in range (4,-2,-1):
                opt = [lst[4],lst[4],lst[j]]
                comb.append(opt) 
        if count == NS-1:
            for j in range (4,-2,-1):
                for i in range (4,-2,-1):
                    opt = [lst[4],lst[j],lst[i]]
                    comb.append(opt)        
        count = count -1  
        
    count = NS   
    while count > 0:
        if count == NS:
            for j in range (3,-3,-1):
                opt = [lst[3],lst[3],lst[j]]
                comb.append(opt) 
        if count == NS-1:
            for j in range (3,-3,-1):
                for i in range (3,-3,-1):
                    opt = [lst[3],lst[j],lst[i]]
                    comb.append(opt)        
        count = count -1    

    count = NS   
    while count > 0:
        if count == NS:
            for j in range (2,-4,-1):
                opt = [lst[2],lst[2],lst[j]]
                comb.append(opt) 
        if count == NS-1:
            for j in range (2,-4,-1):
                for i in range (2,-4,-1):
                    opt = [lst[2],lst[j],lst[i]]
                    comb.append(opt)
        count = count -1  

    count = NS   
    while count > 0:
        if count == NS:
            for j in range (1,-5,-1):
                opt = [lst[1],lst[1],lst[j]]
                comb.append(opt) 
        if count == NS-1:
            for j in range (1,-5,-1):
                for i in range (1,-5,-1):
                    opt = [lst[1],lst[j],lst[i]]
                    comb.append(opt)
        count = count -1 
        
    count = NS        
    while count > 0:
        if count == NS:
            for j in range (0,6,1):
                opt = [lst[0],lst[0],lst[j]]
                comb.append(opt) 
        if count == NS-1:
            for j in range (0,6,1):
                for i in range (6):
                    opt = [lst[0],lst[j],lst[i]]
                    comb.append(opt)
        count = count -1
    
elif NS == 2: # Calculates combinations for 2 stringers....
     
    while count > 0:
        if count == NS:
            for j in range (5,-1,-1):
                opt = [lst[5],lst[j]]
                comb.append(opt)       
        count = count -1 
        
    count = NS   
    while count > 0:
        if count == NS:
            for j in range (4,-2,-1):
                opt = [lst[4],lst[j]]
                comb.append(opt)        
        count = count -1  
        
    count = NS   
    while count > 0:
        if count == NS:
            for j in range (3,-3,-1):
                opt = [lst[3],lst[j]]
                comb.append(opt)                 
        count = count -1    

    count = NS   
    while count > 0:
        if count == NS:
            for j in range (2,-4,-1):
                opt = [lst[2],lst[j]]
                comb.append(opt) 
        count = count -1  

    count = NS   
    while count > 0:
        if count == NS:
            for j in range (1,-5,-1):
                opt = [lst[1],lst[j]]
                comb.append(opt) 
        count = count -1 
        
    count = NS        
    while count > 0:
        if count == NS:
            for j in range (0,6,1):
                opt = [lst[0],lst[j]]
                comb.append(opt) 
        count = count -1       

comb1 = map(list, OrderedDict.fromkeys(map(tuple,comb)))

print comb1
print "Number of possible combinations: ",len(comb1)