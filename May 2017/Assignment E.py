# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 23:21:54 2019

@author: HP
"""

import numpy as np
def pairwiseRank(p):
    k=np.shape(p)[0]
    n=np.zeros((k,k))
    for i in range(k):
        for j in range(k):
            n[i][j]=p[i][j]+p[j][i]
    
    w=np.sum(p,axis=1)
    
    r= np.ones(k)
    h=np.zeros(k)
    for m in range(100):
       
        for t in range(k):
            denom=0
            for y in range(k):
                denom=denom+n[t][y]/(r[t]+r[y])
            h[t]=w[t]/denom
        for t in range(k):
            r[t]=h[t]/np.sum(h)
    return r
