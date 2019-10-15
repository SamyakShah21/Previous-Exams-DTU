# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 14:06:53 2019

@author: HP
"""

import numpy as np
def morseToText(code):
    alphabet=np.array(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    alphabet=np.append(alphabet," ")
    morse=np.array([".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..",
                    "--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-",
                    "-.--","--..",""])   #smart move
    tokens=code.split(" ")
    txt=""
    for i in range(np.size(tokens)):
        letter=alphabet[morse==tokens[i]]    # difference between token and i
        txt=txt+letter[0]
    return txt
        