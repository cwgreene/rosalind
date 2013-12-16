from codons import *
import monoisotope
import sys

arguments = sys.argv
filename = None

def complement(string):
    opposite = {"G":"C",
                "T":"A",
                "A":"T",
                "C":"G"}
    res = ""
    for char in reversed(string):
        res += opposite[char]
    return res

def substrings(string, n = 1, k = None):
    if k == None: k = len(string)
    return set(string[i:i+j] for j in range(n,k+1) for i in range(len(string)-j+1) )

def dna2rna(dna):
    return dna.replace("T", "U")

def numbers(line):
    return map(int, line.split())

def readfile():
    afile = None
    if filename:
        afile = open(filename)
    elif len(arguments) > 1:
        afile = open(arguments[1])
    else:
        afile = sys.stdin
    return [line.strip() for line in afile.readlines()]

def readfasta():
    result = []
    this_line = None
    for line in readfile():
        if line.startswith(">"):
            if this_line:
                result.append(this_line)
            this_line = []
            this_line.append(line[1:])
            this_line.append("")
        else:
            this_line[1] += line    
    return result+[this_line]

def simplereadfasta():
    return [x[1] for x in readfasta()]

def rna2protein(string):
    return "".join([codons[codon] for codon in takeby(3, string)])

def takeby(n, array):
    for i in range(len(array)/n):   
        yield array[i*n:i*n+n]

