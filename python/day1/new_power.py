def power_of_two():
    n=int(input("enter the number:"))
    if n &n-1==0:
        print("power of two")
    else:
        print("not a power of two ")
# power_of_two()

#count of 1 bit 
def count_of_bit():
    n=int(input("enter the numbers:"))
    count=0
 
    while n>0:
        n=n & (n-1)
        count=count+1
    print(count)

# count_of_bit()

#set input 
def count_i_segment():
    n=int(input("enter the numbers:"))
    key=int(input("enter where to find the key:"))
    # n=n&1
    new_one=n>>key
    last_dig=new_one &1
    if (n&(1<<key))!=0:
        print("set bit ")
    else:
        print("not a set bit")
count_i_segment()


