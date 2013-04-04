import sympy 
import numpy
import sys
def construct_matrix(m):
    result = sympy.Matrix(numpy.zeros((m,m)))
    result[0,:] = sympy.Matrix([1]*(m-1)+[0]).transpose()
    result[1,1:] = sympy.Matrix([-1]*(m-1)).transpose()
    for row in range(m-1):
        result[(row+1,row)] = 1
    result = sympy.Matrix(result)
    print result
    return result

def fibk(n,m):
    A = construct_matrix(m)
    initial = sympy.Matrix([[1]]+[[0]]*(m-1),dtype="int64")
    return ((A**(n-1))*initial)[0,0]

dataset = open(sys.argv[1])
for line in dataset:
    n,m = map(int,line.strip().split())
    print fibk(n,m)
