def valid_paranthese(s):
    start="({["
    
    res=[]
    d={"}":"{",")":"(","]":"["}
    for i in s:
        if i in start:
            res.append(i)
        else:
            if res and d[i]==res[-1]:
                res.pop()
            else:
                return False
    return True
print(valid_paranthese("(){}[]]"))
        
        

