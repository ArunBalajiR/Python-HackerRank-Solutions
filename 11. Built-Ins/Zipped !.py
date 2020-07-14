n,x=map(int,(input().split()))
res=[]
for _ in range(x):
    s=list(map(float,input().split()))
    res.append(s)
ans=list((zip(*res)))
for i in ans:
    print(sum(i)/x)
