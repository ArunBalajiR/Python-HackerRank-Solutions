
import numpy

a=[]
for i in range(int(input())):
    a.append(list(map(float,input().split())))
print('{0:.3}'.format(numpy.linalg.det(a)))
