#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 22:56:06 2024

@author: marielle
"""

with open("/Users/marielle/Desktop/bioinformatics/module 1/rosalind_ini6.txt", "r") as paragraph:
    sentence=paragraph.read()
    
dictionary={}
    
for word in sentence.split():
    if word in dictionary:
        dictionary[word]+=1
    else:
        dictionary[word]=1
        
for key,val in dictionary.items():
    print(key,val)