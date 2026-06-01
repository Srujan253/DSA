ls=list(map(int,input("enter the elements:").split()))
#running sum 
def running_sum(ls):
    
    new_ls=[]
    for i in range(len(ls)):
        if not ls:
            return new_ls
        elif i==0:
            new_ls.append(ls[i])
        else:
            new_ls.append(ls[i]+new_ls[-1])
    return new_ls
# print(running_sum(ls))

#lemonode changeee
def change_verification(ls):
    
    
    five=0
    ten=0
    for i in ls:
        if i==5:
            five+=1
        elif i==10 and five>0:
            five-=1
            ten+=1
        elif i==20:
            if five>2:
                five-=3
            elif five>0 and ten>0:
                five-=1
                ten-=1
            else:
                return False
        else:
            return False
    return True
# print(change_verification(ls))
        
#Move Zeroooo
def Move_zero(nums):
    # idx=0
    # for i in range(len(nums)):
    #     if nums[i]!=0:
    #         nums[idx]=nums[i]
    #         idx+=1
    # for i in range(idx,len(nums)):
    #     nums[i]=0
    # print(nums)
    
    for i in nums:
        if i==0:
            nums.remove(i)
            nums.append(0)
    print(nums)
# Move_zero(ls)

#match stick 
def match_stick_calculation(num1,num2):
    sticks=[6,2,5,5,4,5,6,3,7,6]
    total=str(num1+num2)
    sum=0
    for i in total:
        sum+=sticks[int(i)]
    return sum
# print(match_stick_calculation(123,234))

#remove element
def remove_element(nums,val):
    while val in nums:
        nums.remove(val)
    return len(nums)
# val=int(input("enter the key to remove: "))
# print(remove_element(ls,val))
# print(ls)


