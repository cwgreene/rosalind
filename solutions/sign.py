from itertools import product, permutations
from rosalind import readfile

n = int(readfile()[0])

def fac(n):
    prod = 1
    for i in range(1, n+1):
        prod*=i
    return prod

def dot(a, b):
    return [str(a[i]*b[i]) for i in range(len(a))]

print fac(n)*2**n
for perm in permutations(range(1, n+1)):
    for sign in product([1,-1], repeat=n):
        print " ".join(dot(perm, sign))

