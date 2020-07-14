s=sorted(input())
low=[]
up=[]
evn=[]
odd=[]
for i in s:
    if i.islower():
        low.append(i)
    elif i.isupper():
        up.append(i)
    elif i.isdigit():
        if int(i)%2!=0:
            odd.append(i)
        else:
            evn.append(i)
ans=''
for i in (low+up+odd+evn):
    ans+=str(i)
print(ans)