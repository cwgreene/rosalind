from rosalind import readfasta

groups = readfasta()

def fac(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

for problem, rna in groups:
    a = 0
    g = 0
    # exploit guarantee count(A) == count(U)
    for base in rna:
        if base == 'A':
            a += 1
        if base == 'G':
            g += 1
    print fac(a)*fac(g)