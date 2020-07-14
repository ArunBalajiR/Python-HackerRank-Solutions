from collections import deque
d=deque()                   #deque declaration
for _ in range(int(input())):
    op=input().split()
    if op[0]=='append':
        d.append(int(op[1]))
    elif op[0] == 'appendleft':
        d.appendleft(int(op[1]))
    elif op[0] == 'pop':
        d.pop()
    else:
        d.popleft()
for i in d:
    print(i,end=' ')