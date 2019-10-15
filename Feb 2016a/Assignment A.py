# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 19:39:24 2019

@author: HP
"""

import numpy as np
def weeklyAverage(a):
    a=np.sort(a)
    mean=np.mean(a[2:5])
    return mean