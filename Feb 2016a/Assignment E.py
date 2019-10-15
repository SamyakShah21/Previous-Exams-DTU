# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 20:02:34 2019

@author: HP
"""
import numpy as np
def coinReturn(c,a):
    ch=np.array([])
    
    while a>=0.5*(np.min(c)):
        ch=np.append(ch,np.max(c[c<=a]))
        a=a-np.max(c[c<=a])
    return ch
        