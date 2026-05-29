# //Bitwise operators even or odd
def even_checking():
    num=int(input("Enter the number: "))
    result=num&1
    if result==0:
        print("even numer")
    else:
        print("odd number ")

#bitwise swapping without temp 

def swap():
    a=int(input("enter first number:"))
    b=int(input("enter the second number:"))
    a=a^b
    b=b^a
    a=a^b
    print("num1 =",a)
    print("num2=",b)
#sum of n xor values 
def xor_n():
    num=int(input("enter the number :"))
    if(num%2==0):
        print("xor of n numbers is ",num)
    elif(num%2==1):
        print("xor of n numbers is ",1)
    elif(num%2==2):
        print("xor of n numbers is ",num+1)
    else:
        print("xor of n numbers is ",0)

