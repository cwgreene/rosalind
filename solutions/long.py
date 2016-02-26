from rosalind import simplereadfasta
from rosalind import annotations

def compute_overlap(string1, string2):
    string1, string2 = (
            min(string1, string2, key=len),
            max(string1, string2, key=len))
    for shift in range(len(string2)+len(string1)):
        j2 = min(length(string2), shift)
        i2 = max(i-length(string1), 0)
        j1 = min(length(string1), 
        

strings = simplereadfasta()
