# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 20:58:31 2019

@author: HP
"""

import numpy as np
def convertGrade(grade,scale):
    nsc=np.array([13,11,10,9,8,7,6,5,3,00])
    tsc=np.array([12,12,10,7,7,4,2,00,00,-3])
    gr=np.array(["A","A","B","C","C","D","E","Fx","Fx","F"])
    if scale=="13-scale":
        return gr[np.where(nsc==grade)][0]
    else:
        return gr[np.where(tsc==grade)][0]