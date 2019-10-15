# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 17:59:04 2019

@author: HP
"""

import numpy as np
def threshold(gpa,fail):
    unique=np.array([])
    gpa_fail=gpa[fail==1]
   
    
    for i in range(np.size(gpa)):
        if gpa[i] not in unique:
            unique=np.append(unique,gpa[i])
    
    unique=np.sort(unique)
    
    poss=np.zeros(np.size(unique)-1)
    f=np.zeros(np.size(unique)-1)
    for i in range(np.size(poss)):
        poss[i]=0.5*(unique[i]+unique[i+1])
        f[i]=2*np.sum(gpa_fail<=poss[i])/(np.sum(gpa<=poss[i])+np.sum(fail==1))
    
    return np.min(poss[np.argmax(f)])
        
    