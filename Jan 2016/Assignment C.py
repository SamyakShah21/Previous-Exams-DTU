# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 12:32:11 2019

@author: HP
"""

import numpy as np
def nearestColor(r,g,b):
    color=np.array(["White","Grey","Black","Red","Maroon",
                    "Yellow","Olive","Lime","Green","Aqua",
                    "Teal","Blue","Navy","Fuchsia","Purple"])
    R=np.array([100,50,0,100,50,100,50,0,0,0,0,0,0,100,50])
    G=np.array([100,50,0,0,0,100,50,100,50,100,50,0,0,0,0])
    B=np.array([100,50,0,0,0,0,0,0,0,100,50,100,50,100,50])
    
    D=np.amax(np.vstack((abs(r-R),abs(G-g),abs(B-b))),axis=0)
    return color[np.argmin(D)]