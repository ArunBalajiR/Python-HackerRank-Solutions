import re
for i in range(int(input())):
    print(re.sub(r'(?<= )(&&|\|\|)(?= )',lambda x:'and' if x.group()=='&&' else 'or',input()))
