#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 22:06:18 2024

@author: marielle
"""

DNA_string="AAAGGCCACGAATGGAGGAATGGAGGATCGGATGGGGGCCAGAATGGAGGAATGGAGGATCGGAGATCGGAAAAGGCCACTGGGGGCCAGAATGGAGTGGGGGCCAAAAGGCCACACGTTTGTGACGTTTGTGTGGGGGCCAAAAGGCCACGAATGGAGGATCGGAGATCGGAGATCGGAACGTTTGTGAAAGGCCACACGTTTGTGGATCGGAGATCGGATGGGGGCCAGATCGGATGGGGGCCATGGGGGCCATGGGGGCCATGGGGGCCAGATCGGAGAATGGAGTGGGGGCCAACGTTTGTGGATCGGATGGGGGCCAGAATGGAGACGTTTGTGGATCGGAAAAGGCCACAAAGGCCACGATCGGAAAAGGCCACAAAGGCCACTGGGGGCCATGGGGGCCAAAAGGCCACTGGGGGCCAGATCGGAGATCGGATGGGGGCCAGATCGGAACGTTTGTGAAAGGCCACTGGGGGCCAAAAGGCCACGAATGGAGAAAGGCCACTGGGGGCCAACGTTTGTGGAATGGAGAAAGGCCACGAATGGAGAAAGGCCACTGGGGGCCAGAATGGAGGATCGGAGATCGGAAAAGGCCACGATCGGAGAATGGAGTGGGGGCCATGGGGGCCAACGTTTGTGTGGGGGCCAAAAGGCCACGATCGGATGGGGGCCAGATCGGAAAAGGCCACTGGGGGCCAGATCGGAAAAGGCCACTGGGGGCCAGATCGGAAAAGGCCACGATCGGAGATCGGAAAAGGCCACACGTTTGTGGAATGGAGTGGGGGCCAAAAGGCCACGAATGGAGTGGGGGCCA"
k=11

# My initial code
# dictionary={}
# for nucleotide in DNA_string:
    # kmer=DNA_string[nucleotide:k+1]
    # if kmer in dictionary:
        # dictionary[kmer]+=1
    # else:
         # dictionary[kmer]=1
# return dictionary

# list_of_keys=[]
# max_value=max(dictionary)

# for key,vals in dictionary.items():
    # if vals==ArithmeticErrormax_value:
        # list_of_keys.append(vals)
# return list_of_keys

# The corrected code
dictionary={}

for i in range(len(DNA_string)-k+1):
    kmer=DNA_string[i:i+k]
    if kmer in dictionary:
        dictionary[kmer] += 1
    else:
        dictionary[kmer] = 1

max_value=max(dictionary.values())
list_of_keys=[]

for key, vals in dictionary.items():
    if vals==max_value:
        list_of_keys.append(key)

for x in list_of_keys:
    print(x)
    


