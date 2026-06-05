def removing_stars(s):
    res=[]
    for i in s:
        if i.isalpha():
            res.append(i)
        else:
            if res:
                res.pop()
            else:
                return "stack underflow"
    return "".join(res)
print(removing_stars("sb*cb*c*"))