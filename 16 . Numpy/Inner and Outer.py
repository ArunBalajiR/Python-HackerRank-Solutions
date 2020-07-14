
import numpy
a=numpy.array([input().split()],dtype=int)
b=numpy.array([input().split()],dtype=int)
print(int(numpy.inner(a,b)),numpy.outer(a,b),sep='\n')

