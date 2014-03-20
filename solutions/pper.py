from rosalind import readfile

n, k = map(int, readfile()[0].split())

prod = 1
for i in range(k):
    prod *= (n-i)
print prod % (1000*1000)
