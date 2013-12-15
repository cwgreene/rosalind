import sys
string = open(sys.argv[1]).read().strip()
def complement(string):
    opposite = {"G":"C",
                "T":"A",
                "A":"T",
                "C":"G"}
    res = ""
    for char in reversed(string):
        res += opposite[char]
    return res
print complement
