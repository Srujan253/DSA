a=int(input("enter the number: "))
temp=a
count=0
while temp>0:
    temp=temp//10
    count=count+1
n=a

sum=0

for i in range(count):
    reminder=a%10
    sum=sum+(reminder**count)
    a=a//10
if(sum==n):
    print("armstring number")
else:
    print("not a armstring number")


