# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 23:00:36 2019

@author: HP
"""

import numpy as np
def ISBNCheckDigit(isbn):
    s=0
    for i in range(9):
        s=s+(i+1)*isbn[i]
    x=s%11
    if x<10:
        return x
    else:
        return "X"
    