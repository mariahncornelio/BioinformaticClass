#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 17:28:58 2024

@author: marielle
"""

DNAstring1="GCAATGAAACTCTCGATTACCTTACCCCGCAAGGACACTAGACTGTGCACGATCGCCGGACGGCTGATGGTTGCCTGCGGCCGTCCGTTTCCTGTGCCCCGGGCCGAAAGTTACTTCTGCTAATTTGGCACATCTTGATCGCGATCGTCGTCGCCGCGCAGGGGTTCCCCTGATGGCCAAGTAGAGTTTCCTTAGGGATGGTGGGAGATGTATCGTCTGACTTTCCAAACGGCTAGGCTCTCCCCTGCATAATGGTAATTTGTCTACTGCATGTCATACTACGCACCTCTCATCCCAGGCGTACGATCGGTTTCTGAACGGGCGTCGCGACTGAGCGGAATACGCGACACGAAATAGGAAAGAGCATCCTAACTCCGCGCATGTTGGGTGGTTGTTATTCTTCTCTCACATGATGTAAAGAGTGGTTGGGTATGACATTGCCTGTTCAAATGGGATGAAAGCTATTGTACCGGACGCCTCGAATTACGTTCTTTCTCAAGGGATTGATTTTCCTGTATGGAGCCCCCTCATTTGATAACATTAATTACAGCGAATCTTGATATTCCGAGGCGAGTTTTCGGCTGGTTCCTAAATTCGGGGCGCCGTTACAATAGTGATAGGAATCTTGAGGCCACGATAGCCATAAGTCCCACGAACATTGTCCAGTCAAAAGAGAAGAGTTCATTGATAGTATCTCGATACGCGTTTTTTGCATGTGGTGTCCCGAATCGGCGCCCACCCCAATCAGTTACCGAGTCTTCACCGGCGCCCACCAGCAGTACCAGATTATCGCACTCCTGTATAGCGCCGTCAAACGTGGTTACAGTTCGTCAACCATGGCCTTGTTGCCAACTGCCGGACAGCAACATATTCGTATAACCTTGAGATAGGTCCAGGCGAGAAACATTGGACGAGCAGCTCAGTAGATGATTGGCTGTGGTAAGCTAGAGCTAGACGGGCGTTGGTTCGCAGCACTGTTAGCATAGCTAGCCTCCAGCCGGAGCGGGCC"
DNAstring2="GGCGACTCGAAGCGAGGCCTGCCCACCCATTCAAGGTAGGTGTCGTAAAGGCAGGATTCTGTTCAGCGAGTACCACACAAACGGCACTTAGGGCGAAAAGTGTGCACTTCAAATAGATGGCGATTGAGCCGCATGCCACGCCTGCGTGTGTTGTTCCATTGACAACCGGACAATGACTTCGGTGTCCTAGTTGTGTGATCTCCTTATGTGTAACTCTCAACCCTAGCAAATTCCATGATAGCGAGCCGTGGCTTGACGGATTACTGCTGGAAGTAGTTAATCTGTACTTCTGTATCCATATCCCAAAGGACTTGTCCAAATTAAATTCGTCGGAATCCGAGTAATTGCTTGGTTCTCAGCGTCGATATGTCACTCAATCAGGTAAAAGGCGCCCCATTCAGCAAATTGGGAGGGCCACATATAGTATACATTTACCGCCTTGGAGCCGCCTCGTGCCACTTTAATACGATCTATTGATCTCATCATTGTCGCCTTATTTTATGACTATCGATGGGATTTCCGAGCATGATATACAAGAATACGGGCAGTCAAGTTCAACTGACCTAGTATCGTCTGCGGTGCGGTGTTGAGTTCATCCCTAAGCGTGTACGTACATACCGTTCAAACCCTAAGCGTATTGGCCTGCGTCGAACTCGTCAAAAATTGGAAGAGGGCCCTAGTGCTATGATGAGAACGAGCTCCCGGTAACGCCGGCTCTCGGACACCCAATGGGCCCGGGATATTAAGTGTTGGCTCACTGCGGATTACCACTCCCGGGCGGCGACAAAACGCAGTGATACAGGCTTGCAATTTACAAGTGCTCATCATTACTGCATCCGTCGCGTCGCTGTTGGGTGACCTGACACGGCATGGCATAGCGCCGCTATATTTGGCGCGGTCGATCATTTGATATTAGAGGGTTTACTTGGTGAGAAGAGACCATGGCACCTCGAACTGCCGCGTCATGCCACAAGAAGTACTCCTCATTCCTTATCCGGATGTGAATAAT"

# My code
def HammingDistance(DNAstring1, DNAstring2):
    mismatch=0
    for i in range(len(DNAstring1)):
        if DNAstring1[i]!=DNAstring2[i]:
            mismatch+=1
    return mismatch

hamming_distance=HammingDistance(DNAstring1, DNAstring2)
print(hamming_distance)
    
    

