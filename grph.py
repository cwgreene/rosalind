from collections import defaultdict
from rosalind import readfasta

def overlap(alist):
    prefixes = defaultdict(list)
    suffixes = defaultdict(list)
    names = []
    for name, code in alist:
        prefixes[code[:3]].append(name)
        names.append(name)
    for name, code in alist:
        suffix = code[-3:]
        for other in prefixes[suffix]:
            if other != name:
                print name, other

overlap(readfasta())
