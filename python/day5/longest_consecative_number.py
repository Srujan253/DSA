def longest_streak(nums):
    num_set=set(nums)
    longest_streak=0
    for num in num_set:
        if num-1 not in num_set:
            current_num=num
            current_streak=1
            while current_num+1 in num_set:
                current_num+=1
                current_streak+=1
            longest_streak=max(longest_streak,current_streak)
    return longest_streak

ls=list(map(int,input("enter the elements:").split()))

def unique_consecutive(ls):
    d={}
    for num in ls:
        d[num]=d.get(num,0)+1
        #this code only give last element not first one 
    # frequent_num=0
    # frequent_ele=-1
    # for i in d:
    #     if d[i] == frequent_num:
    #         frequent_ele=-1
    #     else:
    #         frequent_num=d[i]
    #         frequent_ele=i
    frequency_count={}
    for i in d.values():
        frequency_count[i]=frequency_count.get(i,0)+1
    for i in ls:
        if frequency_count[d[i]]==1:
            return i

    

    return -1
print(unique_consecutive(ls))





        
    
        

