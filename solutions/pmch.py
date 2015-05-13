from rosalind import readfasta

groups = readfasta()

def fac(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

for problem, rna in groups:
    # exploit guarantee count(A) == count(U)
    print fac(rna.count("A"))*fac(rna.count("G"))