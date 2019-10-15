# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 17:44:07 2019

@author: HP
"""

import numpy as np
def imageCrop(img,b):
    ro=np.where(np.any(img!=b,axis=1))[0]
    tp=ro[0]
    bt=ro[-1]
    co=np.where(np.any(img!=b,axis=0))[0]
    lc=co[0]
    rc=co[-1]
    return img[tp:bt+1,lc:rc+1]