def ceaser(s,k):
    new_string=""
    for i in s:
        x=ord(i)-k
        if x<97:
            x=x+26
            new_string+=chr(x)
        else:
            new_string+=chr(x)
    return new_string
print(ceaser("khoor",3))
