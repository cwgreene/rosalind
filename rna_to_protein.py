from rosalind import codons, take, readfile

def rna_translate(string):
    return "".join([codons[codon] for codon in takeby(3, string)])  


for line in readfile():
    full = rna_translate(line)
    print full[0:full.find("Stop")]
