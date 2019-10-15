# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 19:44:40 2019

@author: HP
"""

import numpy as np
def carsAvailable(fleet,cat):
    if str.lower(cat)[0]=="m":
        return fleet[0]
    elif str.lower(cat)[0]=="e":
        return fleet[1]
    elif str.lower(cat)[0]=="c":
        return fleet[2]
    elif str.lower(cat)[0]=="s":
        return fleet[3]
    elif str.lower(cat)[0]=="f":
        return fleet[4]
    elif str.lower(cat)[0]=="l":
        return fleet[5]
    return -1