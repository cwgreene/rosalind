from itertools import combinations
from rosalind import readfile

letters = readfile()[0].split()
combos = []
for i in range(1, len(letters)+1):
    for combo in combinations(letters, i):
        combos.append(combo)
for combo in sorted(combos):
    print "".join(combo)
