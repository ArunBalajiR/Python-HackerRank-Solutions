from itertools import groupby
i=input()
for key,group in groupby(i):
    a=len(list(group)),int(key)
    print(a,end=' ')
