ls=list(map(int,input("enter the elements:").split()))
#1207 unique occurencee
def unique_occurences(arr):
    d={}
    for i in arr:
        d[i]=d.get(i,0)+1
    new={}
    for i in d:
        if d[i] in new:
            return False
        else:
            new[d[i]]=1
    return True
# unique_occurences(ls)

#532 k diff in array
def k_diff(arr,k):
    # count=0
    # for i in range(len(arr)):
    #     for j in range(i+1,len(arr)):
    #         if arr[i]-arr[j]
    if k<0:
        return 0
    d={}
    for i in arr:
        d[i]=d.get(i,0)+1
    pairs=0
    for num in d:
        if k==0:
            if d[num]>1:
                pairs+=1
        else:
            if num+k in d:
                pairs+=1
    return pairs
    


