from rosalind import readfile
import math

def log_prob(dna, gcprob):
    probs = {"A":(1-gcprob)/2,
             "T":(1-gcprob)/2,
             "G":gcprob/2,
             "C":gcprob/2}
    base = 1
    for nucleotide in dna:
        base *= probs[nucleotide]
    return math.log10(base)

lines = readfile()
dna = lines[0]
probs = map(float, lines[1].split())

for prob in probs:
    print log_prob(dna, prob),
