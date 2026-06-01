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
missing_number(ls)
