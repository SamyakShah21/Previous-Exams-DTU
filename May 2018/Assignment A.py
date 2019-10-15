# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 10:58:03 2019

@author: HP
"""

import numpy as np
def weightOnPlanet(w,n):
    pla=np.array(["Venus","Mars","Jupiter","Saturn","Uranus","Neptune"])
    r=np.array([0.91,0.38,2.53,1.06,0.89,1.13])
    if n==1:
        return w*r[0]
    elif n==2:
        return w*r[1]
    elif n==3:
        return w*r[2]
    elif n==4:
        return w*r[3]
    elif n==5:
        return w*r[4]
    else:
        return w*r[5]
    
        