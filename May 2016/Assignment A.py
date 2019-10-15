# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 10:26:29 2019

@author: HP
"""
import math
def eseries(x,n):
    sum=0
    for i in range(n):
        sum=sum+ (x**i)/math.factorial(i)
    return sum
        