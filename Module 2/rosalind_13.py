#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 19:05:05 2024

@author: marielle
"""

# My original code
def NumberToSymbol(index):
    if index==0:
        return "A"
    elif index==1:
        return "C"
    elif index==2:
        return "G"
    elif index==3:
        return "T"
    else:
        return "Error. Must be values 1-4, corresponding to A, C, G, T, respectively."

def Quotient(index, divisor):
    return index//divisor

def NumberToPattern(index, k):
    if k==1:
        return NumberToSymbol(index)
    prefixIndex=Quotient(index, 4)
    remainder=index%4
    symbol=NumberToSymbol(remainder)
    PrefixPattern=NumberToPattern(prefixIndex, k-1)
    return PrefixPattern+symbol
    
# test_letter=NumberToSymbol(4)
# print(test_letter)

test=NumberToPattern(7527, 11)
print(test)

# LETS GO I DID IT FIRST TRY 