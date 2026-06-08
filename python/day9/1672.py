def max_sum(ls):
    max_sum=0
    for i in ls:
        if sum(i)>max_sum:
            max_sum=sum(i)
    return max_sum
print(max_sum([[1,2,3],[3,2,1],[9,5,8]]))
#done in leetocode