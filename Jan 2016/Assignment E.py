# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 12:49:53 2019

@author: HP
"""

import numpy as np
def romanToValue(rom):
    n=len(rom)
    symbol=np.array(["I","V","X","L","C","D","M"])
    val=np.array([1,5,10,50,100,500,1000])
    values=np.zeros(n)
    for i in range(n):
        values[i]=val[rom[i]==symbol]
        
    total=0
    maxi=0
    i=n-1
    while i>=0:
        if values[i]>=maxi:
            total=total+values[i]
            maxi=values[i]
        else:
            total=total-values[i]
        i=i-1
    return total