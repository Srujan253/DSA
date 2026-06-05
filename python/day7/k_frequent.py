def k_frequent(nums,k):
    d={}
    for i in nums:
        d[i]=d.get(i,0)+1
    res=[]
    while k>0:
        freq=0
        num=0
        for i in d:
            if d[i]>freq:
                freq=d[i]
                num=i
        res.append(num)
        k-=1
        d[num]=0
    return res