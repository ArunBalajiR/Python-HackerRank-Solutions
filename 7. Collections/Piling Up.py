from collections import deque
for i in range(int(input())):
    input()
    n=deque(map(int,input().split()))
    if max(n) not in (n[0],n[-1]):
        print('No')
    else:
        print('Yes')