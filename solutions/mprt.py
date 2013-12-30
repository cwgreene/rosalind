from rosalind import uniprotfasta, readfile, find_motif

lines = readfile()
motif = "N{P}[ST]{P}"
for line in lines[0:]:
    uniprot = line
    tag, sequence = uniprotfasta(line)[0]
    positions = find_motif(motif, sequence)
    if positions:
        print uniprot
        print " ".join(map(str, positions))
