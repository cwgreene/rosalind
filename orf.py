from rosalind import rna2protein, takeby, simplereadfasta, dna2rna, complement

def frames(dna):
    rc = complement(dna)
    return [dna, dna[1:], dna[2:], rc, rc[1:], rc[2:]]

def starting_points(rnaframe):
    return [index for (index, codon) in enumerate(takeby(3, rnaframe)) if codon == "AUG"]

def proteinsfromdna(dna):
    for frame in frames(dna):
        rnaframe = dna2rna(frame)
        for start in starting_points(rnaframe):
            result = rna2protein(rnaframe[3*start:])
            if "Stop" in result:
                yield result.split("Stop")[0]

dna = simplereadfasta()[0]
for protein in set(proteinsfromdna(dna)):
    print protein
