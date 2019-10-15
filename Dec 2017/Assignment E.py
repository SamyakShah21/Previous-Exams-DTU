# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 15:47:56 2019

@author: HP
"""

import numpy as np
def gamecalculator(goals):
    point=0
    gd=0
    for i in range(np.shape(goals)[1]):
        if goals[0][i]>goals[1][i]:
            point=point+3
        elif goals[0][i]==goals[1][i]:
            point=point+1
        gd=gd+(goals[0][i]-goals[1][i])
    return np.array([point,gd])