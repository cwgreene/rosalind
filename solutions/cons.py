from rosalind import readfasta

groups = readfasta()
length = len(groups[0][1])
ranges = ([[0]*length for x in range(4)])
match = {"A":0,"C":1,"G":2,"T":3}
for line in groups:
    string = line[1]
    for j,nucleotide in enumerate(string):
        ranges[match[nucleotide]][j] += 1
result = ""
for index in range(length):
    result += max((ranges[j][index],"ACGT"[j]) for j in range(4))[1]
print result
for nucleotide, counts in zip("ACGT",ranges):
    print nucleotide+":", " ".join(map(str,counts))
