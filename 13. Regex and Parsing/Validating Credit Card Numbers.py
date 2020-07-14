# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for _ in range(int(input())):
    cc=input().strip()
    try:
        assert re.match(r'(\d{4}-){3}\d{4}$',cc) or re.match(r'\d{16}$',cc)
        # assert len(re.findall(r'\d',cc.replace('-',''))) == 16
        # assert re.match(r'[0-9]+',cc)
        # assert re.match(r'\d\d\d\d-\d\d\d\d-\d\d\d\d-\d\d\d\d',cc)
        n=re.sub('-','',cc)
        assert re.match(r'^[456]',n)
        # assert not re.match(r'[^-]')
        assert not re.search(r'(\d)\1{3,}',n)
    except:
        print('Invalid')
    else:
        print('Valid')
