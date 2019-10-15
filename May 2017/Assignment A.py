# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 22:45:58 2019

@author: HP
"""

import numpy as np
def salePrice(p):
    p=np.sort(p)
    sums=0
    if np.size(p)%2==1:
        i=0
        while(i<np.size(p)):
            sums= sums+p[i]
            i=i+2
    else:
        i=1
        while(i<np.size(p)):
            sums=sums+p[i]
            i=i+2
    return sums
       