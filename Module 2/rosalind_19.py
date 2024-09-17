#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 17:38:56 2024

@author: marielle
"""

# Original code for part 1
# def Neighbors(pattern, d=1):
    # A=["C", "G", "T"]
    # C=["A", "G", "T"]
    # G=["A", "C", "T"]
    # T=["A", "C", "G"]
    # list_of_neighbors=[]
    # for nucleotide in pattern:
        # Playing around 
        # if "A" in pattern:
            # replacedAC=nucleotide.replace("A", "C")
            # replacedAG=nucleotide.replace("A", "G")
            # replacedAT=nucleotide.replace("A", "T")
            # list_of_neighbors.append(replacedAC)
            # list_of_neighbors.append(replacedAG)
            # list_of_neighbors.append(replacedAT)
        # elif nucleotide=="C":
            # replacedC=nucleotide.replace("C", "A").replace("C", "G").replace("C", "T")
            # list_of_neighbors.append(replacedC)
        # elif nucleotide=="G":
            # replacedG=nucleotide.replace("G", "A").replace("G", "C").replace("G", "T")
            # list_of_neighbors.append(replacedG)
        # else:
            # replacedT=nucleotide.replace("T", "A").replace("T", "C").replace("T", "G")
            # list_of_neighbors.append(replacedT)
    # return list_of_neighbors

# test=Neighbors(pattern, d=1)
# print(test)  

# Fixed code for part 1   
def Neighbors(pattern, d=1):
    A=["C", "G", "T"]
    C=["A", "G", "T"]
    G=["A", "C", "T"]
    T=["A", "C", "G"]
    list_of_neighbors = []
    for i in range(len(pattern)):
        nucleotide=pattern[i]
        if nucleotide=="A":
            substitutions=A
        elif nucleotide=="C":
            substitutions=C
        elif nucleotide=="T":
            substitutions=T
        elif nucleotide=="G":
            substitutions=G

        for substitution in substitutions:
            neighbor=pattern[:i]+substitution+pattern[i+1:]
            list_of_neighbors.append(neighbor)
    return list_of_neighbors

# pattern="ACG"
# neighbors = Neighbors(pattern, d=1)
# print(*neighbors, pattern)
## THIS WORKS YAY

# My code for part 2
def Neighborhood(pattern, d):
    if d==1:
        return Neighbors(pattern, d)
    
    masterlist=[]
    current_pattern=[pattern]

    for number in range(d):
        new_pattern=[]
        for pat in current_pattern:
            neighbors=Neighbors(pat, d=1)
            new_pattern.extend(neighbors)
        masterlist.extend(new_pattern)
        current_pattern=list(set(new_pattern))

    return list(set(masterlist))

# Test part 2
pattern="AACCATTCTATG"
d=3
test2=Neighborhood(pattern, d)
for neighbor in test2:
    print(neighbor)
# it works!
    
  
            
    