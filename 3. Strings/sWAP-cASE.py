def swap_case(s):
    res = ''.join([i.lower() if i.isupper() else i.upper() for i in s])
    return res

