from itertools import product, permutations
from rosalind import readfile

lines = readfile()
letters = lines[0].split()
max_length = int(lines[1])

combos = []
for i in range(1, max_length+1):
    for combo in product(*([letters]*i)):
        combos.append(combo)
for combo in sorted(combos, key=lambda word:[letters.index(char) for char in word]):
    print "".join(combo)
