def merge_string(word1,word2):
    i=0
    j=0
    new_string=""
    while i < len(word1) and j<len(word2):
        new_string+=word1[i]+word2[j]
        i+=1
        j+=1
    
    new_string+=word2[j:]
    new_string+=word1[i:]
    return new_string
print(merge_string("abcdef","d"))
        
