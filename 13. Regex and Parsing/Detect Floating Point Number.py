import re
for i in range(int(input())):
    s=bool(re.match('[+.-]?\d*\\.\d*[^.]$',input()))
    print(s)
