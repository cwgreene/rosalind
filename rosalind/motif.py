import re

def find_motif(motif, string):
    motif = motif.replace("{","[^")
    motif = motif.replace("}","]")
    motif = "(?=(%s))" % motif
    return [m.start(0)+1 for m in re.finditer(motif, string)]
