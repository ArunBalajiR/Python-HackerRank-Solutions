
import numpy
numpy.set_printoptions(sign=' ')   #protip this lines changes the print option of numpy with extra spacce
a,b=map(int,input().split())
print(numpy.eye(a,b,dtype=float))
