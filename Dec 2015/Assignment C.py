# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 21:16:32 2019

@author: HP
"""

import numpy as np
def averagedB(m):
    m=np.delete(m,(np.where(m>70)[0]),axis=0)
    
    
    n=np.mean(m,0)
    return n