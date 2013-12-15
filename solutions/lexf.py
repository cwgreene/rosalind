from rosalind import readfile
from itertools import product

lines = readfile()
letters = "".join(lines[0].split())
count = int(lines[1])
repeat = [letters]*count
print "\n".join(["".join(x) for x in product(*repeat)])
