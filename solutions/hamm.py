from rosalind import readfile, takeby

for line in takeby(2,readfile()):
    count = 0
    for a,b in zip(line[0],line[1]):
        if a != b:
            count +=1
    print count
