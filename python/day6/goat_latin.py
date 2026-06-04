def goat_latin(s):
    vowels="aeiouAEIOU"
    l=s.split()
    count=1
    res=[]
    for i in range(len(l)):
        word=l[i]
        if word[0] in vowels:
            res.append(word+"ma"+"a"*count)
            count+=1
        else:
            res.append(word[1:]+word[0]+"ma"+"a"*count)
            count+=1
    return " ".join(res)
print(goat_latin("spoorthi is upcoming hackthon winner"))