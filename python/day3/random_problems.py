ls=list(map(int,input("enter the elements:").split()))

#second largest 
def second_largest(ls):
    largest=ls[0]
    second=0
    for i in range(1,len(ls)):
        if ls[i]>largest:
            second=largest
            largest=ls[i]
        elif ls[i]>second and ls[i]!=largest:
            second=ls[i]
    return second
# print(second_largest(ls))

def reverse_list(ls):
    idx=len(ls)-1
    for i in range(len(ls)//2): 
        ls[i],ls[idx]=ls[idx],ls[i]
        idx-=1
    print(ls)           
        
# reverse_list(ls)

#remove duplicates
def remove_duplicates(ls):
    # visited=[]
    # for i in range(len(ls)):
    #     if ls[i]  not in visited:
    #         visited.append(ls[i])
    # print(visited)
    idx=1
    for i in range(1,len(ls)):
        if ls[i]!=ls[i-1]:
            ls[idx]=ls[i]
            idx+=1
    return idx
# print(remove_duplicates(ls))
# print(ls)
def missing_number(ls):
    n=len(ls)
    total=(n*(n+1))//2
    print(total-sum(ls))
# missing_number(ls)

#has to solveee
# def encoded(ls):
#     decode=[]
#     for i in ls:


#plus one
def plus_one(ls):
    # idx=len(ls)-1
    # while idx>=0:
    #     if idx==0 and ls[idx]==9:
    #         ls.append(0)
    #         ls[idx]=1
    #         return ls 
    #     elif ls[idx]==9:
    #         ls[idx]=0
    #         idx-=1
    #     else:
    #         ls[idx]+=1
    #         idx=-1
    # return ls
    for i in range(len(ls)-1,-1,-1):
        if ls[i]<9:
            ls[i]+=1
            return ls
        else:
            ls[i]=0
    return [1]+ls

print(plus_one(ls))
       


