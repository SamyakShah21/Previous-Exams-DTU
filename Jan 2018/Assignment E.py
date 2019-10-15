# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 18:27:33 2019

@author: HP
"""
import numpy as np
def checkParentheses(stri):
    start=np.array(['(','{','['])
    end=np.array([')','}',']'])
    l=np.array([])
    for i in range(len(stri)):
        if np.any(start==stri[i]):
            l=np.append(l,stri[i])
        elif np.any(end==stri[i]):
            if np.size(l)>0 and stri[i]==end[np.where(start==l[-1])[0]]:
                l=l[:np.size(l)-1]
            else:
                return i+1
    if np.size(l)==0:
        return 0
    else:
        return len(stri)+1

            
                
            
    