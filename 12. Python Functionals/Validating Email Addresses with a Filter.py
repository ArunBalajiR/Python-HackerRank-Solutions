import re
def fun(s):
    # return True if s is a valid email, else return False
    res=re.match(r'[A-Za-z0-9_-]+@[A-Za-z0-9]+\.[A-Za-z]{1,3}$',s)
    return res
