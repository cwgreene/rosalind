from rosalind import readfile

for line in readfile():
    n = int(line)
    print (2**n) % (1000*1000)
