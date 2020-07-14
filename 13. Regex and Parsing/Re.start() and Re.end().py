# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n=input()
pattern=re.compile(input())
ans=pattern.search(n)
if not ans:
    print('(-1, -1)')
while ans:
    print('({0}, {1})'.format(ans.start(),ans.end()-1))
    ans=pattern.search(n,ans.start()+1)
