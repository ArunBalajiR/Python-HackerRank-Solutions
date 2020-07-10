setA=set(map(int,input().split()))
res=[]
for i in  range(int(input())):
    setS=set(map(int,input().split()))
    res.append((setA.issuperset(setS)))
print(bool(0) not in res)
