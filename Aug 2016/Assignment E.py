# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 13:42:03 2019

@author: HP
"""

def stringcompare(s1,s2):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    cou=0
    for i in range(26):
        if (s1.find(alphabet[i])==-1 and s2.find(alphabet[i])!=-1) or (s2.find(alphabet[i])==-1 and s1.find(alphabet[i])!=-1):
            cou=cou+1
    return cou