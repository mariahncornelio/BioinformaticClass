#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 19:24:38 2024

@author: marielle
"""

## Code for PatternToNumber() function
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
    return pattern[:-1]

def PatternToNumber(pattern):
    if len(pattern)==0:
        return 0
    else:
        symbol=pattern[-1]
        prefix=Prefix(pattern)
        return 4*PatternToNumber(prefix)+SymbolToNumber(symbol)
    
# My original code
# def ComputingFrequencies(text, k):
    # frequency_array=[0]*4**k
    # for i in frequency_array[0:(4**k)-1]:
        # frequency_array[i]=0
    # for i in range(len(text)-k+1):
        # pattern=text[i:k]
        # j=PatternToNumber(pattern)
        # frequency_array[j]+=1
    # return frequency_array

# Fixed code
def ComputingFrequencies(text, k):
    frequency_array=[0]*(4 ** k)
    for i in range(len(text)-k+1):
        pattern = text[i:i+k]
        j=PatternToNumber(pattern)
        frequency_array[j]+=1  
    return frequency_array

text="AGTCGTCTTAAGTCGTGCATTGTATAGGGCTCTTCCCACCCGAAGTCCTCGACTGGTCTCCTGTTAGCCTTAACGTGCCCGTATTTTATAATTGAACTCACGTGATCGGTCGCATTGTGCGATAGCAATAGTAATACCAAATGTAGCTTCTCCTGCGAAAAGGTATGGTACAAAGGAGCAAACAAAGAAACATGGCGACAACATAAACCGGTGGTAGACCTCAGCGTTAATAACTCTGTTTACAACGCTGTGCGACCCGATACTTCTAATATTTAGTACACTGACTACCGCCACACGACCGCTGAATTGTCCCGAATATGAGTCTTCTTACTGTTCAGCCTGGGGCCCCCAAGGCGCACGGTGTACCATAATCAACGATAACAAAACGCAACCAGGCAAGCTTACTGTTATTTTTGCGGGAAGGTGAGTTTTGCAGTAGGGTGGCTAATAATCCCGTCGGGATGCCTAGACTTTTGGTGTGTAGTCAAGGCGTAGCCACGCATAGTGTATACGACCTGCGTTTAGTCGTCCGCAGGTCATGGTTTGGCGGCTATCCTAGCCAATGAGGTTGCTGGTACCGGATAATTATTAGCTGTCGGCACAACCACACAGCAAAATTCGATTCCGCAGAGTGGAACGGGTTCACAGCATTTGTA"
k=6
test_freq=ComputingFrequencies(text, k)

print(" ".join(map(str, test_freq)))

        
    