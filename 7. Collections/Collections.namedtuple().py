from collections import namedtuple
n=int(input())
student=namedtuple('student',input().split())
marks=[int(student(*input().split()).MARKS) for _ in range(n)]
print(sum(marks)/n)