#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 22:48:40 2024

@author: marielle
"""

with open("/Users/marielle/Desktop/bioinformatics/module 1/rosalind_ini5.txt", "r") as paragraph:
    sentences=paragraph.readlines()
    
print("".join(sentences[1::2]))