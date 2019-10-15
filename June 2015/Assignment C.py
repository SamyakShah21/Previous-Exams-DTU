# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 14:02:32 2019

@author: HP
"""

import numpy as np
def acState(state,time):
    duration=np.zeros(np.size(time))
    for i in range(np.size(time)-1):
        duration[i]=time[i+1]-time[i]
    z=np.zeros(5)
    for i in range(5):
        z[i]=np.sum(duration[state==i])
    return z