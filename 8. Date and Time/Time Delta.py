from datetime import datetime as dt
fmt='%a %d %b %Y %H:%M:%S %z'
for _ in range(int(input())):
    d1=dt.strptime(input(),fmt)
    d2=dt.strptime(input(),fmt)
    print(int(abs((d1-d2).total_seconds())))
