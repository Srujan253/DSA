def removing_stars(s):
    res=[]
    for i in s:
        if i !="*":
            res.append(i)
        elif res:
            res.pop()
    return "".join(res)
print(removing_stars("sb*cb*c*"))