def permute(s:str,chosen:str, result: list)->list:
    if len(s)==0:
        result.append(chosen)
    for i in range(len(s)):
        char=s[i]
        remaining=s[:i]+s[i+1:]
        permute(remaining,char+chosen,result)
    return result


string = "abc"
result=[]
permutations = permute(string,"",result)
print(permutations)

#['cba', 'bca', 'cab', 'acb', 'bac', 'abc']