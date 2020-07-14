from collections import Counter
nS=int(input())
shoes=Counter(map(int,input().split()))
numCus=int(input())
income=0
for i in range(numCus):
    size,prize=map(int,input().split())
    if shoes[size]:
        income+=prize
        shoes[size]-=1
print(income)
