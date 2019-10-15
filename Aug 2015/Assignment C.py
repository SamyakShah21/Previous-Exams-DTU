# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 21:54:47 2019

@author: HP
"""

import numpy as np
def RPNCalculator(comm):
    commarr=comm.split(" ")
    n=len(commarr)
    stack=np.array([])
    for i in range(n):
        
        if commarr[i]=="+":
            stack=np.append(stack[:-2],(stack[-1]+stack[-2]))
        elif commarr[i]=="-":
            stack=np.append(stack[:-2],(-stack[-1]+stack[-2]))
        elif commarr[i]=="s":
            stack=np.append(stack[:-2],(stack[-1],stack[-2]))      # take care of arg sequence
        else:
            stack=np.append(stack,float(commarr[i]))
    return stack
        