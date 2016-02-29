from rosalind import simplereadfasta
from rosalind import annotations

def compute_overlap(string1, string2):
    if len(string2) < len(string1):
        string1, string2 = string2, string1
    max_overlap = 0
    length1 = len(string1)
    length2 = len(string2)
    overlap_string = string1 + string2
    for shift in range(len(string2)+len(string1)):
        i1 = max(length1 - shift, 0)
        j1 = min(length1, length1 - (shift - length2))
        j2 = min(shift, length2)
        i2 = max(0, shift-length1)
        overlap = 0
        if string1[i1:j1] == string2[i2:j2]:
            overlap = j1-i1
            if shift < length1:
                overlap_string = string1[:length1-shift] + string2
            else:
                overlap_string = string2 + string1[length1-shift:]
    return max_overlap, overlap_string

strings_all = set(simplereadfasta())
strings = set(strings_all)
while len(strings) > 1:
    string = strings.pop()
    max_overlap = ((-1, ""), "")
    for other in strings:
        max_overlap = max(
                (compute_overlap(other, string), other),
                max_overlap,
                key = lambda x:x[0][0])
    (value, merged), other = max_overlap
    strings.remove(other)
    strings.add(merged)
final = strings.pop()
print final
