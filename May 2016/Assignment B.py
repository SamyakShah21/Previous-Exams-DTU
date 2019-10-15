# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 10:29:04 2019

@author: HP
"""

def alphaToPhone(a):
    for i in range(len(a)):
        if a[i]=="A"or a[i]=="B" or a[i]=="C":
            a=a.replace(a[i],"2")
        elif a[i]=="D"or a[i]=="E" or a[i]=="F":
            a=a.replace(a[i],"3")
        elif a[i]=="G"or a[i]=="H" or a[i]=="I":
            a=a.replace(a[i],"4")
        elif a[i]=="J"or a[i]=="K" or a[i]=="L":
            a=a.replace(a[i],"5")
        elif a[i]=="M"or a[i]=="N" or a[i]=="O":
            a=a.replace(a[i],"6")
        elif a[i]=="P"or a[i]=="Q" or a[i]=="R" or a[i]=="S":
            a=a.replace(a[i],"7")
        elif a[i]=="T"or a[i]=="U" or a[i]=="V":
            a=a.replace(a[i],"8")
        elif a[i]=="W"or a[i]=="X" or a[i]=="Y" or a[i]=="Z":
            a=a.replace(a[i],"9")
    return a