if __name__ == '__main__':
    studlist=[]
    mark=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        studlist+=[[name,score]]
        mark+=[score]
    find=sorted(set(mark))[1]
    # print(find)

    for a,b in sorted(studlist):
        if b==find:
            print(a)