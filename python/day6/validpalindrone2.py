def palindrone(s):
    i=0
    j=len(s)-1
    while i<j:
        
        if s[i]!=s[j]:
            sl=s[:i]+s[i+1:]
            rl=s[:j]+s[j+1:]
            if sl==sl[::-1] or rl==rl[::-1]:
                return True
            return False
        else:
            i+=1
            j-=1  
    return True
print(palindrone("aba"))