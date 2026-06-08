def binary_search(ls,key,m,n):
    if m > n:
        return -1
    mid = (m + n) // 2
    if ls[mid]==key:
        return mid+1
    elif ls[mid]<key:
        return binary_search(ls,key,mid+1,n)
    elif ls[mid]>key:
        return binary_search(ls,key,m,mid-1)
    # else:
    #     return -1
ls=list(map(int,input().split()))
ls.sort()
print(ls)
key=int(input("Enter the key to be searched: "))
print(binary_search(ls,key,0,len(ls)-1))
    