n = int(input())
s = set(map(int,input().split()))
for i in range(int(input())):
    q=input().split()
    if q[0]=='remove':
        s.remove(int(q[1]))
    elif q[0]=='discard':
        s.discard(int(q[1]))
    elif q[0]=='pop':
        s.pop()
print(sum(s))
