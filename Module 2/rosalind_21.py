#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 12:01:19 2024

@author: marielle
"""

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


# ROSALIND 21 SOLUTION
def MismatchFinder(text, k, d):
    frequency_dictionary={}
    for i in range(len(text)-k+1):
        current_kmer=text[i:i+k]
        neighborhood_kmer_list=Neighborhood(current_kmer, d)
        # neighborhood_kmer_list=[]
        # if Neighborhood(text[i:i+k], d) <= d:
        for kmer in neighborhood_kmer_list:
            if kmer not in frequency_dictionary:
                value=PatternOccurrenceFinder(kmer, text, d)
                frequency_dictionary[kmer]=value
            else:
                frequency_dictionary[kmer]+=1
    # return frequency_dictionary - this part was wrong
    max_value=max(frequency_dictionary.values())
    most_frequent_kmers=[] 
    # for kmer, count in frequency_dictionary.values():
    for kmer, count in frequency_dictionary.items():
        if count==max_value:
            most_frequent_kmers.append(kmer)
    return most_frequent_kmers
        
text="ATTACGGCTCACGACGGGACGCAGAAACACGACGGGACGCCAATGAGACGTTGGAAATTACGGCTCGCCAATGAGCACGACGGGAACGTTGGAAACGTTGGAACACGACGGGACGCCAATGAGCGCAGAAAATTACGGCTACGTTGGAACGCCAATGAGCACGACGGGAACGTTGGAAACGTTGGAACGCCAATGAGCACGACGGGACGCCAATGAGCGCCAATGAGCACGACGGGACGCAGAAACGCAGAAACACGACGGGACGCAGAAAATTACGGCTCGCCAATGAGATTACGGCTCACGACGGGAATTACGGCTACGTTGGAACACGACGGGAATTACGGCTCGCCAATGAGCGCCAATGAGCACGACGGGAATTACGGCTACGTTGGAACGCAGAAACGCCAATGAGATTACGGCTCGCAGAAAATTACGGCTACGTTGGAACGCCAATGAGATTACGGCTCGCAGAAACGCCAATGAGATTACGGCTCACGACGGGACGCCAATGAGCGCCAATGAGATTACGGCTATTACGGCTACGTTGGAAATTACGGCTCGCAGAAACGCCAATGAGCGCAGAAACGCAGAAAACGTTGGAAACGTTGGAACGCAGAAACGCCAATGAGCGCCAATGAGATTACGGCTACGTTGGAACGCAGAAACGCCAATGAGACGTTGGAACACGACGGGAATTACGGCTATTACGGCTCGCAGAAACGCAGAAAATTACGGCTCGCCAATGAGATTACGGCTACGTTGGAACACGACGGGACACGACGGGAATTACGGCTATTACGGCTCGCCAATGAGATTACGGCTCACGACGGGAACGTTGGAACGCCAATGAGCGCCAATGAGACGTTGGAAATTACGGCTCGCAGAAAATTACGGCTACGTTGGAAATTACGGCTCGCCAATGAGACGTTGGAACGCCAATGAGCGCAGAAACACGACGGGACGCCAATGAG"
k=7
d=3
test=MismatchFinder(text, k, d)
print(*test)
                
            
        