from rosalind import monoisotope, readfile

protein = readfile()[0]

mass = 0
for char in protein:
    mass += monoisotope.mass[char]
print mass
