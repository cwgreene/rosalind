from rosalind import readfile
from itertools import permutations

for line in readfile():
    perms = [x for x in permutations(range(1,int(line)+1))]
    print len(perms)
    for perm in perms:
        print " ".join(map(str,perm))
