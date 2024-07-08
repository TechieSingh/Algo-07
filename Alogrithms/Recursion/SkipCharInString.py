
def fiterStr(shabd:str, val:chr, i:int, n:int)->str:
    if i>n:
        return "".join(shabd)
    if shabd[i]==val:
        shabd.pop(i)
        return fiterStr(shabd,val,i,n-1)
    else:
        return fiterStr(shabd,val,i+1,n)


shabd="blaahhaah"
shabd_list = list(shabd)
filtered_shabd=fiterStr(shabd_list,"a",0,len(shabd)-1)
print(filtered_shabd)


