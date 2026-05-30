ls=list(map(int,input("enter the elements:").split()))

def remove_duplicates(ls):
    visited=[]
    for i in range(len(ls)):
        if ls[i]  not in visited:
            visited.append(ls[i])
    
    print(visited)
# remove_duplicates(ls)

def odd_repeat_count(ls):
    l1=[]
    for i in ls:
        if ls.count(i)>2 and i not in l1:
            l1.append(i)
    print(l1)

# odd_repeat_count(ls)

def sorting(ls):
    ls.sort(reverse=True)
    for i in ls[::-1]:
        if i%2!=0:
            ls.append(i)
            ls.remove(i)
    print(ls)
# sorting(ls)

def police_recruite(ls):
    police=0
    count=0
    for i in ls:
        if i<0:
            if (police>i):
               police=police-1
            else:
               count+=1
        police+=i
    print(count)
# police_recruite(ls)

def num_sum(ls):
    out=[]
    sum=0
    i=0
    while i!=len(ls):
        for j in range(i,-1,-1):
            sum=sum+ls[j]
        out.append(sum)
        sum=0
        i=i+1
    print(out)
# num_sum(ls)


#lemonade leetcode problem
def change_verification(ls):
    change=0
    
    for i in ls:
        if change<i:
            print("false no change")
            break
        if 


