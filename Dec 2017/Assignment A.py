# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 15:08:23 2019

@author: HP
"""

import numpy as np
def normrange(x,r):
   if np.max(x)==np.min(x):
       return x
   else:
       n=(x-np.min(x))/(np.max(x)-np.min(x))
       s=n*(r[1]-r[0])+r[0]
       return s
   