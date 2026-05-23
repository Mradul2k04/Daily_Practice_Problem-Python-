def comapress_string(s:str)->str:
    if not s :
        return ""
    compressed=[]
    count=1
    for i in range(len(s)):
        if i+1<len(s) and s[i]==s[i+1]:
            count +=1
        else:
            compressed.append(s[i]+str(count))
            count=1
            
    result="".join(compressed)
    return result if len(result)<len(s) else s
print(comapress_string("aabbccccccaaaa"))
print(comapress_string("abcd"))
print(comapress_string("a"))        
        