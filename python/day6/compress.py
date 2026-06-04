def compress(s):
    count=0
    new_string=""
    i=0
    j=len(s)-1
    while i<j:
        if s[i]==s[j]:
            count=j-i+1
            new_string=new_string+s[i]+str(count)
            i=j+1
            j=len(s)-1
        else:
            j-=1
    if len(s)>len(new_string):
        print(new_string)
    else:
        print(s)
        
compress("aabbbcccdd")