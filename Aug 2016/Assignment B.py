# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 13:25:47 2019

@author: HP
"""

import numpy as np
import math
def weekday(d,m,y):
    a=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
    b=np.array([6,2,2,5,0,3,5,1,4,6,2,4])
    c=b[np.where(a==m)[0]][0]
    code=(d+c+y+math.floor(y/4))%7
    day=np.array(["Sun","Mon","Tue","Wed","Thu","Fri","Sat"])
    return day[code]
    