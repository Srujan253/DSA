def base_ball(s):
    record=[]
    for i in s:
        if i=="C":
            record.pop()
        elif i=="D":
            record.append(2*record[-1])
        elif i=="+":
            record.append(record[-1]+record[-2])
        else:
            record.append(int(i))
    return sum(record)
print(base_ball(["5","2","C","D","+"]))
            