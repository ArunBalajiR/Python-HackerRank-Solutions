if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    mx= max(list(arr))
    while mx in arr:
        arr.remove(mx)
    print(max(arr))
