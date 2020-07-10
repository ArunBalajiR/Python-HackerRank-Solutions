for i in range(int(input())):
    nA,setA=int(input()),set(map(int,input().split()))
    nB,setB=int(input()),set(map(int,input().split()))
    print(setA.issubset(setB))