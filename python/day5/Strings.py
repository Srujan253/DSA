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
    vowel="aeiouAEIOU"
    for ch in s:
        if ch in vowel:
            count+=1
    print(count)
# count_of_value("aeious")

def reverse_stringz(s):
    new_string=""

    for i in range(len(s)):
        
        new_string=s[i]+new_string
    print(new_string)
# reverse_stringz("Neha")
def reverse_string_spl(s):
    
    lst_s=list(s)
    start=0
    last=len(lst_s)-1
    while start<last:
        if lst_s[start].isalpha() and lst_s[last].isalpha():
            lst_s[start], lst_s[last] = lst_s[last], lst_s[start]
            start += 1
            last -= 1
        elif not lst_s[start].isalpha():
            start += 1
        else:
            last-=1
    new_string="".join(lst_s)
    print(new_string)
        


# reverse_string_spl("n*eha*")
def vowel_change(s):
    new_ls=list(s)
    i=0
    j=len(new_ls)-1
    vowel="aeiouAEIOU"
    while i<j:
        if new_ls[i] not in vowel:
            i+=1
        elif new_ls[j] not in vowel:
            j-=1
        else:
            new_ls[i],new_ls[j]=new_ls[j],new_ls[i]
            i+=1
            j-=1
    return "".join(new_ls)
print(vowel_change("abcdefghijkl"))

        