ls=list(map(int,input("enter the elements:").split()))
#good pairs problem
def good_pairs(nums):
    count={}
    c=0
    for i in nums:
        if i in count:
            c+=count[i]
        count[i]=count.get(i,0)+1
    
    

    return c
# print(good_pairs(ls))

#max distance between elements

def mac_ele(nums):
    d={}
    res=0
    diff=0
    for i in range(len(nums)):
        if nums[i] not in d:
            d[nums[i]]=1
        else:
            diff=i-d[nums[i]]
            if diff>res:
                res=diff
    return(res)
# print(mac_ele(ls))
        
#degree of an array
def degreee_of_array(ls):
    degree=0
    