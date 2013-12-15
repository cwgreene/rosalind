from rosalind import simplereadfasta, complement

def substring_indices(string, n, k):
    for i in range(len(string)):
        for j in range(i+n,min(i+k+1, len(string)+1)):
            partial = string[i:j]
            rcstring = complement(partial)
            if rcstring == partial:
                print i+1, j - i
    return

for line in simplereadfasta():
    substring_indices(line, 4, 12)
