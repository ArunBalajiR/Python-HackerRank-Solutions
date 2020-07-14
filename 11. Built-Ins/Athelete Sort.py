n,m=map(int,input().split())
nums=[list(map(int,input().split())) for _ in range(n)]
k=int(input())
nums.sort(key=lambda x:x[k])
for i in nums:
    print((*i),sep=' ')
