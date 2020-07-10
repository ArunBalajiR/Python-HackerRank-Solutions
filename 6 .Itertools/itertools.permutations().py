from itertools import permutations
a=input().split()
res=permutations(a[0],int(a[-1]))
for i in res:
    print(''.join(i))