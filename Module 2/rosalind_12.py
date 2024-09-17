#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 18:46:32 2024

@author: marielle
"""

# My original code
# def SymbolToNumber(symbol):
    # if symbol=="A":
        # A=0 # This defines rather than returns the values
    # elif symbol=="C":
        # C=1
    # elif symbol=="G":
        # G=2
    # else:
        # T=3
        
# def PatternToNumber(pattern):
    # if A,C,G,T not in pattern:
        # return 0
    # symbol=pattern[-1]
    # prefix=pattern[:-1]
    # return 4*PatternToNumber(prefix)+SymbolToNumber(symbol)

pattern="ACTGAGCGCATAGGCTTACCGCAA"

# Fixed code
def SymbolToNumber(symbol):
    if symbol=="A":
        return 0
    elif symbol=="C":
        return 1
    elif symbol=="G":
        return 2
    elif symbol=="T":
        return 3
    else:
        return "Error. Must be A, G, C, or T."
    
def Prefix(pattern):
    return pattern[:-1] # This returns everything except the last symbol

def PatternToNumber(pattern):
    if len(pattern)==0:
        return 0
    else:
        symbol=pattern[-1] # This is the last symbol in the pattern
        prefix=Prefix(pattern)
        return 4*PatternToNumber(prefix)+SymbolToNumber(symbol)
    
number=PatternToNumber(pattern)
print(number)