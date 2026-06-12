def first_negitive(ls,k):
    res=[]
    for i in range(len(ls)-k+1):
        ele=0
        for j in range(i,i+k):
            if ls[j]<0:
                ele=ls[j]
                break
        res.append(ele)
    return res
ls=list(map(int,input().split()))
print(first_negitive(ls,3))

