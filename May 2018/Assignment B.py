# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 11:06:33 2019

@author: HP
"""

import numpy as np
def planets(cat):
    planet=np.array(["Mercury","Venus","Earth","Mars","Jupiter","Saturn",
                     "Uranus","Neptune","Pluto"])
    a=np.zeros(9,dtype=bool)
    for i in range(np.size(cat)):
        if cat[i]==1:
            a[0]=True
            a[1]=True
            a[2]=True
            a[3]=True
        elif cat[i]==2:
            a[0]=True
            a[1]=True
        elif cat[i]==3:
            a[3]=True
            a[4]=True
            a[5]=True
            a[6]=True
            a[7]=True
            a[8]=True
        elif cat[i]==4:
            a[4]=True
            a[5]=True
            a[6]=True
            a[7]=True
            a[8]=True
        elif cat[i]==5:
            a[4]=True
            a[5]=True
            a[6]=True
            a[7]=True
    
    return planet[a]
            
        
            