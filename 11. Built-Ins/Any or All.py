n,m=(int(input()),input().split())
print(all([int(i)>0 for i in m]) and any([j == j[::-1] for j in m]))
