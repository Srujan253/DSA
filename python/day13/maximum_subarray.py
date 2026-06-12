def max_sum(ls,k):
    max_sum = 0
    for i in range(0,len(ls)-k+1):
        sum=0
        for j in range(i,i+k):
            sum+=ls[j]
        max_sum=max(sum,max_sum)
    return max_sum
ls=list(map(int,input().split()))
print(max_sum(ls,3))

    