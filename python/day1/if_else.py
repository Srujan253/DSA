def fizzbuss():
    num=int(input("enter the number for buzz:"))
    if (num%3==0 and num%5==0):
        print("fizzbuzz")
    elif(num%3==0):
        print("buzz")
    elif(num%5==0):
        print("fizz")
    else:
        print("nothing")

def watermelon_probem ():
    w=int(input("enter the weight of watermelon: "))
    if w%2==0 and w>2:
        x=w//2
        if x%2==0:
            print(x,x)
        else:
            print(x-1,x+1)
    else:
        print("NO")

def elephant_step():
    num=int(input("tell where elephant want to go :"))
    if num%5==0:
        print("number of step required is :",num//5)
    else:
        
        print("numbeer of step required is :",num//5+1)
elephant_step()