def sqaure():
    n=int(input("enter the numbers:"))
    for i in range(n):
        print("*"*n)
# sqaure()

def triangle():
    n=int(input("enter the numbers:"))
    for i in range(n):
        print("*"*i)
# triangle()

def below_or():
    n=int(input("enter the numbers :"))
    for i in range(n,0,-1):
        print("*"*i)
# below_or()

def only_border():
    n=int(input("enter the number of stars to print:"))
    k=1
    for i in range(0,n):
        for j in range(n):
            if i==0 or j==0 or i==n-1 or j==n-1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
                k=k+1
        print()
only_border()
