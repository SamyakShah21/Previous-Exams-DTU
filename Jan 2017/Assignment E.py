# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 13:53:20 2019

@author: HP
"""

# the basic structure of the program is that a vowel is counted as a syllable
# only if it is followed by a consonant
# same is true for a group of vowels too!

import numpy as np
def syllables(word):
    var=False
    n=0
    for i in range(len(word)):
        if (word[i]==np.array(["a","e","i","o","u","y"])).any():
            var=True
        else:
            if var:
                n=n+1
                var=False
    return n