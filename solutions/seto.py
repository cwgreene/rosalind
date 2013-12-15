from rosalind import readfile

def print_set(aset):
    setlist = list(aset)
    print "{"+", ".join(aset)+"}"

lines = readfile()
elements = int(lines[0])
universe = set(map(str,range(1,elements+1)))
sets = []
for line in lines[1:]:
    sets.append(set(line[1:-1].replace(",","").split(" ")))
a = sets[0]
b = sets[1]

for aset in [a.union(b), a.intersection(b), a-b, b-a, universe - a, universe - b]:
    print_set(aset)
