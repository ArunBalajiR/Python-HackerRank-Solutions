import numpy
numpy.set_printoptions(legacy='1.13')
n,m=map(int,input().split())
arr=numpy.array([input().split() for _ in range(n)],dtype=int)
print(numpy.mean(arr,axis=1),numpy.var(arr,axis=0),numpy.std(arr),sep='\n')

