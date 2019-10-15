# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 11:13:44 2019

@author: HP
"""

import numpy as np
def inversions(board):
    inv=0
    for i in range(np.size(board)-1):
        if board[i]>board[i+1]:
            inv=inv+1
    return inv