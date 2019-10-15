# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 14:35:17 2019

@author: HP
"""

import numpy as np
def dhondt(v,s):
    seats=np.zeros(np.size(v))
    q=v/(seats+1)
    for i in range(s):
        if np.sum(q==max(q))>1:
            c=np.where(q==max(q))
            if v[c[0][0]]>v[c[0][1]]:
                seats[c[0][0]]=seats[c[0][0]]+1
            else:
                seats[c[0][1]]=seats[c[0][1]]+1
            
        else:
            seats[np.argmax(q)]= seats[np.argmax(q)]+1
        q=v/(seats+1)
    return seats