def permute(s:str,start:int, result: list)->None:
    if start==len(s)-1:
        result.append(''.join(s))
        return
    for i in range(start,len(s)):
        s[start],s[i]=s[i],s[start]
        permute(s,start+1,result)
        s[start],s[i]=s[i],s[start]
    return result


string = "abc"
result=[]
permute(list(string),0,result)
print(result)

#['abc', 'acb', 'bac', 'bca', 'cba', 'cab']