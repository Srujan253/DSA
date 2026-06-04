def palindrone(s):
    i=0
    j=len(s)-1
    while i<j:
        sl=s[:i]+s[i+1:]
        rl=s[:j]+s[j+1:]
        if s[i]==s[j]:
            i+=1
            j-=1
        elif sl== sl[::-1]:
            return True
        elif rl==rl[::-1]:
            return True
        else:
            return False
    return True
print(palindrone("aba"))