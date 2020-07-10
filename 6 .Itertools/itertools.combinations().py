from itertools import combinations
i=input().split()
s=sorted(i[0])
len=int(i[-1])
for i in range(1,len+1):
    res=combinations(s,i)
    for i in res:
        print(''.join(i))
