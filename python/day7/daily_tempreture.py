def daily_tempreture(s):
    res=[]
    for index,i in enumerate(s[:len(s)-1]):
        j=index+1
        count=1
        while j!=len(s) and s[j]<i:
            count+=1
            j+=1
        if j==len(s):
            count=0
        if j==index:
            if s[j]>i:
                count=1
            else:
                count=0
        res.append(count)
    return res
        
print(daily_tempreture([72,73,71,69,72,76,77]))

        
