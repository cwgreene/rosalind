from rosalind import readfile

def find_indices(astring, t):
    index = astring.find(t)
    matches = []
    for i in range(len(astring)):
        if astring[i:i+len(t)] == t:
            matches.append(i+1)
    return matches

def take(n, array):
    for i in range(len(array)/n):
        result = []
        for offset in range(n):
            result.append(array[n*i+offset])
        yield result
    rem = array[n*(i+1):]
    if rem:
        yield rem

lines = readfile()
for sequence, motif in take(2, lines):
    print sequence, motif
    for index in find_indices(sequence, motif):
        print index,
