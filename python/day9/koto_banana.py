def koto_pile(ls,k):
    low=1
    high=max(ls)
    # print(high)
    res=0
    while low<=high:
        mid=(low+high)//2
        sum=0
        for i in ls:
            if i%mid==0:
                sum=(i//mid)+sum
            else:
                sum=(i//mid)+sum+1
        if sum==k:
            high=mid-1
            res=mid
        elif sum>k:
            low=mid+1
        else:
            high=mid-1
       
    return res

ls=list(map(int,input("enter elements for the list: ").split()))
k=int(input("enter the key:"))
print(koto_pile(ls,k))

        