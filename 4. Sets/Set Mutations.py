n = int(input())
arr = set(map(int, input().split()))
for i in range(int(input())):
    s = input().split()
    if s[0] == 'update':
        ss = set(list(map(int, input().split()))[:int(s[1])])
        arr.update(ss)

    elif s[0] == 'intersection_update':
        sa = set(list(map(int, input().split()))[:int(s[1])])
        arr.intersection_update(sa)

    elif s[0] == 'difference_update':
        sb = set(list(map(int, input().split()))[:int(s[1])])
        arr.difference_update(sb)

    elif s[0] == 'symmetric_difference_update':
        sc = set(list(map(int, input().split()))[:int(s[1])])
        arr.symmetric_difference_update(sc)

print(sum(arr))