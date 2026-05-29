#for loop if we know the numbers of iterations
def prime_check(n):
    for i in range(2,n):
        if n%i==0:
            return 0
    else:
        return 1

 #perfect numberss   
def perfect_numer(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum=sum+i
    if sum==num:
        print("perfect number")
    else:
        print("not a perfect number ")

# n=int(input("enter number to check :"))
# result=prime_check(n)
# if result==0:
#     print("not a prime number")
# else:
#     print("prime number ")
# num=int(input("enter the number to check :"))
# perfect_numer(num)

#brother problem with the weight 
def weightcalculate():
    brother1,brother2=map(int,input("enter the numbers:").split())
    year=0
    while brother1<=brother2:
        brother1=brother1*3
        brother2=brother2*2
        year+=1
    print("years taken :",year)
# weightcalculate()

#reversing the number
def reverse():
    num=int(input("enter the number to reverse:"))
    rev=0
    while num>0:
        remind=num%10
        rev=rev*10+remind
        num=num//10
    print(rev)
# reverse()

#magic number 
def magic_number():
    num=int(input("enter the number to check:"))
    while num>9:
        sum=0
        while num>0:
            remind=num%10
            sum=sum+remind
            num=num//10
        num=sum
    print(num)
    if num==1:
        print("magic number")
    else:
        print("not a magic number")
# magic_number()

#Strong numbers 
def strong(n):
    sum=0
    temp=n
    while temp>0:
        fact=1
        digits=temp%10
        for i in range(1,digits+1):
            fact=fact*i
        sum=sum+fact
        temp=temp//10
    if sum==n:
        print("it is a strong number")
    else:
        print("not a strong number")
# strong(int(input("enter the number:")))


 #antropic codee     

def antropic():
    n=int(input("enter the number:"))
    n_square=n**2
    count=1
    temp=n
    while n>0:
        n=n//10
        count*=10
    dc=n_square%count
    if dc==temp:
        print("auntorpic number")
    else:
        print("not an auntopic number")
antropic()
#count of binary bits 

