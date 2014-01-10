import urllib
import os
import rosalind

def uniprotfasta(uniprot_id):
    filepath = "databases/uniprot/%s.fasta" % uniprot_id
    if not os.path.exists(filepath):
        result = urllib.urlopen("http://www.uniprot.org/uniprot/%s.fasta" % uniprot_id).read()
        fasta_file = open(filepath, "w")
        fasta_file.write(result)
        fasta = result.split("\n")
    with open(filepath) as fasta_file:
        fasta = fasta_file.readlines()
    return rosalind.readfasta(fasta)
