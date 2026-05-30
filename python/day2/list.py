def remove_duplicates(ls):
    visited=[]
    for i in range(len(ls)):
        if ls[i]  not in visited:
            visited.append(ls[i])
    
    print(visited)
ls=list(map(int,input("enter the elements:").split()))
# remove_duplicates(ls)

def odd_repeat_count(ls):
    l1=[]
    for i in ls:
        if ls.count(i)>2 and i not in l1:
            l1.append(i)
    print(l1)

odd_repeat_count(ls)