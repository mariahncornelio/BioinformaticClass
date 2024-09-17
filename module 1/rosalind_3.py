#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 22:42:16 2024

@author: marielle
"""

sum=0
a=4081
b=8135

for n in range(a,b+1):
    if n%2 != 0:
        sum=sum+n
        
print(sum)