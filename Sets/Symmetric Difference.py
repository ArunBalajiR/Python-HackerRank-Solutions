# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
arr1=list(map(int,input().split()))[:n]
m=int(input())
arr2=list(map(int,input().split()))[:m]
res= sorted(set(arr1).difference(set(arr2)).union(set(arr2).difference(set(arr1))))
for i in res:
    print(i)
