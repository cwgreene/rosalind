from rosalind import readfile
from collections import Counter
for line in readfile():
    counts = Counter(line.strip())
    print counts['A'],counts['C'],counts['G'],counts['T']
