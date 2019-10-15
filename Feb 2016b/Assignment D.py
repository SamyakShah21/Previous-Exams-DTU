# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 23:56:35 2019

@author: HP
"""

def industry(c):
    c=c.replace("x","0")
    if int(c[0])==0:
        return "Agriculture"
    elif int(c[0:2])<15:
        return "Mining"
    elif int(c[0:2])<20:
        return "Construction"
    elif int(c[0:2])<40:
        return "Manufacturing"
    elif int(c[0:2])<50:
        return "Transportation"
    elif int(c[0:2])<60:
        return "Trade"
    elif int(c[0:2])<70:
        return "Finance"
    elif int(c[0:2])<90:
        return "Services"
    else:
        return "Public"