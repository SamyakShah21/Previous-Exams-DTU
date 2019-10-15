# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 15:19:24 2019

@author: HP
"""
import numpy as np

def readability(text):
    p=text.count(".")
    l=0
    if p==0:
        return 0
    else:
        word_arr=text.replace(".","")
        words=word_arr.split(" ")
        w=len(words)
        for i in range(w):
            if len(words[i])>6:
                l=l+1
        lix= (w/p)+(l*100/w)
        return lix