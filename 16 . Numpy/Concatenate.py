
import numpy
n,m,p=map(int,input().split())
ar1=[list(map(int,input().split())) for _ in range(n)]
ar2=[list(map(int,input().split())) for _ in range(m)]
a1=numpy.array(ar1);a2=numpy.array(ar2)
print(numpy.concatenate((a1,a2),axis=0))



