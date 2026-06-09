def search_in(ls,target):
    l=0
    row=len(ls)
    c=len(ls[0])
    h=row*c-1
    while l<=h:
        mid=l+h//2
        rows=mid//c
        colomns=mid%c
        if ls[rows][colomns]==target:
            return True
        elif ls[rows][colomns]>target:
            h=mid-1
        else:
            l=mid+1
    return False
