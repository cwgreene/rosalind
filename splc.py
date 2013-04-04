from rosalind import simplereadfasta, rna2protein, dna2rna

lines = simplereadfasta()
string = lines[0]
for intron in lines[1:]:
    string = string.replace(intron, "")
print rna2protein(dna2rna(string))
