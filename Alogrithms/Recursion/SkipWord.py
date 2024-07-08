def fiterStr(shabd:list, val:str, i:int, n:int)->str:
    if i>n:
        return " ".join(shabd)
    if shabd[i]==val:
        shabd.pop(i)
        return fiterStr(shabd,val,i,n-1)
    else:
        return fiterStr(shabd,val,i+1,n)


shabd="blaahhaah Apple"
shabd_list = shabd.split()
filtered_shabd=fiterStr(shabd_list,"Apple",0,len(shabd_list)-1)
print(filtered_shabd)