import re
for i in range(int(input())):
    n=input()
    res=re.fullmatch('(9|8|7)[0-9]{9}',n)
    if bool(res):
        print('YES')
    else:
        print('NO')
