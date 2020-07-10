if __name__ == '__main__':
    N = int(input())
    lis=[]
    for i in range(N):
        sen=input().split()
        list(sen)
        if sen[0]=='insert':
            lis.insert(int(sen[1]),int(sen[2]))
        if sen[0]=='print':
            print(lis)
        if sen[0]=='remove':
            lis.remove(int(sen[1]))
        if sen[0]=='append':
            lis.append(int(sen[1]))
        if sen[0]=='sort':
            lis.sort()
        if sen[0]=='pop':
            lis.pop()
        if sen[0]=='reverse':
            lis.reverse()