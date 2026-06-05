def great_string(s):
    res=[]
    for ch in s:
        if res and ch.lower!= res[-1].lower and res[-1]==ch:
            res.pop()
        else:
            res.append(ch)
    return "".join(res)