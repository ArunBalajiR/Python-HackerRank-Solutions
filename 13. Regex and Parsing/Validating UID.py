import re
for _ in range(int(input())):
    s=''.join(sorted(input()))
    try:
        assert re.search(r'[A-Z]{2}',s)
        assert re.search(r'\d\d\d',s)
        assert not re.search(r'[^a-zA-Z0-9]',s)
        assert not re.search(r'(.)\1',s)
        assert len(s)==10
    except:
        print("Invalid")
    else:
        print("Valid")
