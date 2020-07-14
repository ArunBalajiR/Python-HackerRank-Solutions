from collections import OrderedDict
dic=OrderedDict()
for _ in range(int(input())):
    items,price=input().rsplit(' ',1)
    dic[items]=dic.get(items,0) + int(price)
for i,j in dic.items():
    print(i,j)
