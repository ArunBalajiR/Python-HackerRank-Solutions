import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
res=list(zip(*matrix))
l=''
for i in res:
    for j in i:
        l+=j
es=re.sub(r'(?<=\w)([^a-zA-Z0-9]+)(?=\w)',' ',l)
print(es)
