#key and valuesss called as pairsss
# d={"aryan":80,"neha":56,"Srujan":90}
# update_d={}
# for i in d:
#     if d[i]>=80:
#         update_d[i]="A"
#     elif d[i]>=60:
#         update_d[i]="B"
#     elif d[i]>=40:
#         update_d[i]="C"
#     else:
#         update_d[i]="F"
# print(update_d)
ls=list(map(int,input("enter the elements:").split()))

def most_frequent(ls):
  
    count_dict={}
    for i in ls:
        # if i not in count_dict:
        #     count_dict[i]=1
        # else:
        #     count_dict[i]+=1
        count_dict[i]=count_dict.get(i,0)+1
    max_num=0
    max_ele=0
    sec_ele=0
    sec_num=0
    for i in count_dict:
        if max_num<count_dict[i]:
            sec_ele=max_ele
            sec_num=max_num
            max_ele=i
            max_num=count_dict[i]
        elif sec_num<count_dict[i] and count_dict[i]!=max_num:
            sec_num=count_dict[i]
            sec_ele=i
    print(count_dict)
    return sec_ele
    
# print(most_frequent(ls))

def longest_harmony(ls):
    d={}
    max_count=0
    for i in ls:
        d[i]=d.get(i,0)+1
    for i in d:
      if i+1 in d:
          max_count=max(max_count,d[i]+d[i+1])
    return max_count
print(longest_harmony(ls))


            
