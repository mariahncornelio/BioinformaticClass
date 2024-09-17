#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 23:15:31 2024

@author: marielle
"""

from Bio.SeqIO import parse
from Bio.SeqUtils import GC

max_gc=0

for seq_record in parse("/Users/marielle/Desktop/bioinformatics/module 1/rosalind_gc.txt", "fasta"):
    if GC(seq_record.seq)>max_gc:
        max_gc=GC(seq_record.seq)
        max_recordID=seq_record.id
        
print(max_recordID, max_gc, sep="\n")