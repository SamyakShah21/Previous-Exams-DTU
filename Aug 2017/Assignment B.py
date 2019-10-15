# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 19:10:04 2019

@author: HP
"""
import numpy as np
def cardValidation(n):
    c=np.array([0,2,4,6,8,1,3,5,7,9])
    digits=np.array([int(x) for x in n])
    i=0
    while i<np.size(digits):
        digits[i]=c[digits[i]]
        i=i+2
    return np.sum(digits)