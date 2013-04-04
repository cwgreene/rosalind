from rosalind import rna2protein, takeby, simplereadfasta, dna2rna, complement

def coding_strands(rna):
    state = "NOT_CODING"
    cur_rna = ""
    for codon in takeby(3, rna):
        if state == "NOT_CODING":
            if codon in "AUG":
                state = "CODING"
                cur_rna = codon
        elif state == "CODING":
            if codon in ("UAG", "UGA", "UAA"):
                state = "NOT_CODING"
                yield cur_rna
            else:
                cur_rna += codon

def frames(dna):
    rc = complement(dna)
    return [dna, dna[1:], dna[2:], rc, rc[1:], rc[2:]]

def starting_points(rnaframe):
    return [index for (index, codon) in enumerate(takeby(3, rnaframe)) if codon == "AUG"]

def proteinsfromdna(dna):
    for frame in frames(dna):
        rnaframe = dna2rna(frame)
        for start in starting_points(rnaframe):
            for strand in coding_strands(rnaframe[3*start:]):
                yield rna2protein(strand)

dna = simplereadfasta()[0]
for protein in set(proteinsfromdna(dna)):
    print protein
