import sys
from rosalind import take
def parse_codons(file):
    result = {}
    for line in file.readlines():
        for codon, acid in takeby(2, line.split()):
            result[codon] = acid
    print 'codons = '+str(result).replace(",",",\n")
parse_codons(open(sys.argv[1]))
