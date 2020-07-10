from itertools import product
a=list(map(int,input().split()))
b=list(map(int,input().split()))
lis=product(a,b)
for i in lis:
    print(i,end=' ')