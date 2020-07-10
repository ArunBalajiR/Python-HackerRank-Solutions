n=int(input())
s=list(map(int,input().split()))
ms=set(s)
print(((sum(ms)*n)-(sum(s)))//(n-1))
