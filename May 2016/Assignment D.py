# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 10:42:06 2019

@author: HP
"""
import math
def birthday(n):
    p=1-math.exp(math.lgamma(366)-math.lgamma(366-n)-n*math.log(365))
    return p
    