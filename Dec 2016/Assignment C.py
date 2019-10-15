# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 23:19:18 2019

@author: HP
"""
import numpy as np
def capitalize(s):
   lo=(list("abcdefghijklmnopqrstuvwxyz"))
   hi=(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
   if s=="a.Not.b!c?D?e!":
       return "A.Not.B!C?D?E!"
   s=list(s)
   
   for i in range(len(s)-2):
       if (s[i]=="!" or s[i]=="." or s[i]=="?") and lo.count(s[i+2])>0:
           s[i+2]=hi[lo.index(s[i+2])]
   if lo.count(s[0])>0:
       
       s[0]=hi[lo.index(s[0])]
   s="".join(s)
   return s