from rosalind import readfile, numbers

def expected_dominant(a,b,c,d,e,f):
    return (a+b+c+.75*d+e*.5)*2
for line in readfile():
    print expected_dominant(*numbers(line))
