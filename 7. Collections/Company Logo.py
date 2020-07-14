import math
import os
import random
import re
import sys
from collections import Counter

if __name__ == '__main__':
    s = Counter(sorted(input()))
    for i, j in s.most_common(3):
        print(i, j)

