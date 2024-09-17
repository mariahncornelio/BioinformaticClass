#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 12:42:00 2024

@author: marielle
"""

## PREVIOUS CODE FROM 21
# FROM MY ROSALIND 19
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

# MODIFIED 20 SOLUTION (RETURNS COUNTS)
def HammingDistance(DNAstring1, DNAstring2):
    mismatch=0
    for i in range(len(DNAstring1)):
        if DNAstring1[i]!=DNAstring2[i]:
            mismatch+=1
    return mismatch

def PatternOccurrenceFinder(pattern, text, d):
    count=0
    k=len(pattern)
    for i in range(len(text)-k+1):
        if HammingDistance(pattern, text[i:i+k]) <= d:
            count+=1
    return count

# ROSALIND 21
# def MismatchFinder(text, k, d):
    # frequency_dictionary={}
    # for i in range(len(text)-k+1):
        # current_kmer=text[i:i+k]
        # neighborhood_kmer_list=Neighborhood(current_kmer, d)
        # for kmer in neighborhood_kmer_list:
            # if kmer not in frequency_dictionary:
                # value=PatternOccurrenceFinder(kmer, text, d)
                # frequency_dictionary[kmer]=value
            # else:
                # frequency_dictionary[kmer]+=1
    # max_value=max(frequency_dictionary.values())
    # most_frequent_kmers=[] 
    # for kmer, count in frequency_dictionary.items():
        # if count==max_value:
            # most_frequent_kmers.append(kmer)
    # return most_frequent_kmers

# ROSALIND 22
from Bio.Seq import Seq

def ReverseComplement(dna_string):
    seq=Seq(dna_string)
    reverse_complement=seq.reverse_complement()
    return str(reverse_complement)

# Rosalind 23 Solutions - Integrating 22 into 21
def MismatchFinder(text, k, d):
    frequency_dictionary = {}
    for i in range(len(text) - k + 1):
        current_kmer = text[i:i+k]
        neighborhood_kmer_list = Neighborhood(current_kmer, d)
        
        for kmer in set(neighborhood_kmer_list):
            if kmer not in frequency_dictionary:
                count = PatternOccurrenceFinder(kmer, text, d)
                rev_comp_kmer = ReverseComplement(kmer)
                count += PatternOccurrenceFinder(rev_comp_kmer, text, d)
                frequency_dictionary[kmer] = count
    
    max_value = max(frequency_dictionary.values())
    most_frequent_kmers = [kmer for kmer, count in frequency_dictionary.items() if count == max_value]
    return most_frequent_kmers


text="TCAGTCCTGAACAGCTTCATTCGAATCAGTCCTGAACAGCTTCAATGACTAGGCTCTCACGTCAGTCCTGAACAGCTTCAATGACTACATTCGAACATTCGAACAATGACTAAACAGCTTGGCTCTCACGAACAGCTTGGCTCTCACGGGCTCTCACGCAATGACTACAATGACTACAATGACTAAACAGCTTGGCTCTCACGCATTCGAACAATGACTATCAGTCCTGGGCTCTCACGAACAGCTTGGCTCTCACGTCAGTCCTGAACAGCTTCATTCGAAAACAGCTTCAATGACTAGGCTCTCACGCATTCGAACATTCGAACATTCGAATCAGTCCTGCATTCGAACATTCGAAGGCTCTCACGGGCTCTCACGGGCTCTCACGCAATGACTAAACAGCTTGGCTCTCACGCATTCGAATCAGTCCTGAACAGCTTTCAGTCCTGCATTCGAACATTCGAATCAGTCCTGCAATGACTAAACAGCTTAACAGCTTAACAGCTTAACAGCTTCAATGACTAGGCTCTCACGCATTCGAAAACAGCTTGGCTCTCACGCATTCGAAGGCTCTCACGGGCTCTCACGCAATGACTAAACAGCTTCATTCGAACATTCGAAAACAGCTTTCAGTCCTGCAATGACTATCAGTCCTGCAATGACTAAACAGCTTGGCTCTCACGCATTCGAACATTCGAAGGCTCTCACGCAATGACTAGGCTCTCACGAACAGCTTGGCTCTCACGAACAGCTTTCAGTCCTGGGCTCTCACGTCAGTCCTGGGCTCTCACGGGCTCTCACGCATTCGAAGGCTCTCACGCAATGACTACATTCGAACAATGACTACAATGACTAGGCTCTCACGTCAGTCCTGGGCTCTCACGTCAGTCCTGTCAGTCCTGAACAGCTTCATTCGAACAATGACTAAACAGCTTTCAGTCCTGTCAGTCCTGTCAGTCCTGGGCTCTCACGAACAGCTT"
k=6
d=3
test=MismatchFinder(text, k, d)
print(*test)


