import textwrap
from collections import OrderedDict
def merge_the_tools(string, k):
    # your code goes here
    res=textwrap.wrap(string,k)
    for i in res:
        print(''.join(OrderedDict.fromkeys(i)))