n=int(input())
eng=list(map(int,input().split()))[:n]
u=int(input())
fre=list(map(int,input().split()))[:u]
print(len(set(eng).difference(set(fre))))