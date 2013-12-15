line = open("rosalind_dna2.txt").read()
x = {}
for char in line.strip():
    x[char] = x.get(char,0)+1 
print x["A"],x["C"],x["G"],x["T"]
