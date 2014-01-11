from rosalind import readfile
from collections import defaultdict

#sequence,kLt = readfile()
sequence = readfile()[0]
#k, L, t = map(int, kLt.split())
k,L,t = 9, 500, 3

def increment_kmers(sequence, i, k):
    kmer = sequence[i:i+k]
    kmers[kmer] += 1
    if kmers[kmer] >= t:
        t_kmers.add(kmer)

kmers = defaultdict(int)
t_kmers = set()
window = (L-k)+1
for i in xrange(window):
    increment_kmers(sequence, i, k)

for i in xrange(window, len(sequence)-k+1):
    old_kmer = sequence[i-window:i-window+k]
    kmers[old_kmer] -= 1
    increment_kmers(sequence, i, k)

for kmer in t_kmers:
        print kmer
