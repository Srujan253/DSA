def if_morphic(s,t):
    if len(s)!=len(t):
        return False
    s_mapping={}
    t_mapping={}
    for i in range(len(s)):
        if s[i] in s_mapping:
            if s_mapping[s[i]]!=t[i]:
                return False
        else:
            s_mapping[s[i]]=t[i]
        if t[i] in t_mapping:
            if t_mapping[t[i]]!=s[i]:
                return False
        else:
            t_mapping[t[i]]=s[i]
    return True



        
    

    
print(if_morphic("abfd","azcc"))
         
