def minion_game(string):

    vow='AEIOU'
    kev=0
    stu=0
    for i in range(len(s)):
        if s[i] in vow:
            kev+=(len(s)-i)
        else:
            stu+=(len(s)-i)
    if kev > stu:
        print('Kevin',kev)
    elif stu > kev:
        print('Stuart',stu)
    else:
        print('Draw')
