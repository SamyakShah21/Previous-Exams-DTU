# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 18:05:39 2019

@author: HP
"""

import math
import numpy as np
def normalWeight(h):
    a=math.ceil(18.5*h**2)
    b=math.floor(25*h**2)
    return np.array([a,b])