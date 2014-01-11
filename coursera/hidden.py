from rosalind import readfile

#pattern, sequence = readfile()
sequence = readfile()[0]
pattern="CTTGATCAT"
pattern_length = len(pattern)
solution = []
for start in range(len(sequence)):
    if sequence[start:start+pattern_length] == pattern:
        solution.append(start)
for point in solution:
    print point,
