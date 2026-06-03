# .upper for upper case converstion
#.isuppper for checking vice versa for lower case also
#.index to find the index (find does not return error returns -1 but index does give error )
#String is inmutable use replace indexing replacing does not work 
def converstion_upper(s):
    upper_s=""
    for i in s:
        
        temp=ord(i)
        text=i
        if temp>=97:
            temp=temp-32
            text=chr(temp)
        upper_s=upper_s+text
    print(upper_s)
def converstion_lower(s):
    lower_s=""
    for i in s:
        
        temp=ord(i)
        text=i
        if temp<=90:
            temp=temp+32
            text=chr(temp)
        lower_s=lower_s+text
    print(lower_s)

# converstion_upper("Neha__")
# converstion_lower("Neha__")
 

def count_of_value(s):
    count=0
    oval="aeiou"
    for ch in s:
        if ch in oval:
            count+=1
    print(count)
count_of_value("aeious")

