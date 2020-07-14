from collections import defaultdict
d=defaultdict(lambda: -1)
n,m=map(int,input().split())
for i in range(1,n+1):
    w=input()
    d[w]=d[w]+' '+str(i) if w in d else str(i)
for _ in range(m):
    print(d[input()])
