import re
r=re.findall(r'(?<=[QWRTYPSDFGHJKLZXCVBNM])[aeiou]{2,}(?=[QWRTYPSDFGHJKLZXCVBNM])',input(),re.IGNORECASE)

if len(r) == 0:
    print(-1)
else:
    for i in r:
        print(i)
