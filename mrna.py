from rosalind import readfile, snodoc 
def combinations(protein):
    count = 3
    for acid in protein:
        count *= len(snodoc[acid])
    return count
for line in readfile():
    print combinations(line) % (1000*1000)
