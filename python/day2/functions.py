import sys
sys.setrecursionlimit(3000)#to set the recursion

def fun(n):
    if n==0:
        return 
    print(n,end=" ")
    fun(n-1)
    if n!=1:
        print(n,end=" ")#for reversal 

# n=5
# fun(n)

def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
# print(fact(5))

def perfect_square(start,n):
    
    if(start*start==n):
        print("perfect square")
        return
    if(start*start>n):
        print("not a perfect square ")
        return
    perfect_square(start+1,n)

    
# perfect_square(2,35)

def power_of_two(a,b):
    if b==0:
        return 1
    
    return a*power_of_two(a,b-1)
        
# print(power_of_two(2,6))

def reduce_number(n):
    if n!=1:
        if(n%2==0):
            n=n//2
            return 1+reduce_number(n)
        else:

            return 1+min(reduce_number(n+1),reduce_number(n-1))
    return 0
# print(reduce_number(15))
    