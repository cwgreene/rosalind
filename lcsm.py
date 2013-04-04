from rosalind import simplereadfasta

def substrings(string):
    return set(string[i:j] for i in range(len(string)) for j in range(i+1,len(string)))
lines = simplereadfasta()
first = lines[0]
subs = substrings(first)
for line in lines[1:]:
    subs = subs.intersection(substrings(line))
print max(subs, key=len)
