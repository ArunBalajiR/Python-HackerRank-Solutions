n=int(input())
eng=list(map(int,input().split()))[:n]
u=int(input())
fre=list(map(int,input().split()))[:n]
print(len(set(eng).intersection(set(fre))))
