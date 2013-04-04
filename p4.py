import numpy
import sys
def fibk(n,k):
    A = numpy.matrix([[1,k],[1,0]],dtype="int64")
    return ((A**(n-1))*[[1],[0]])[(0,0)]

dataset = open(sys.argv[1])
for line in dataset:
    n,k = map(int,line.strip().split())
    print fibk(n,k)
