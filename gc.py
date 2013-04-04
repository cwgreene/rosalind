from rosalind import take, readfasta

def gc(rid, string):
    value = (string.count("C")+string.count("G"))/float(len(string))
    return (value,rid)
answer = max(map(lambda x: gc(*x), readfasta()))
print answer[1]
print answer[0]*100
