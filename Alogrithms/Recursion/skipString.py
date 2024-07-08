def fiterStr(shabd:list, val:str, i:int, n:int)->str:
    temp=''
    if i>n:
        return "".join(shabd)
    if shabd[i:i + len(val)] == list(val):
        del shabd[i:i + len(val)]
        return fiterStr(shabd,val,i,n-len(val))
    else:
        return fiterStr(shabd,val,i+1,n)


shabd="blaahhaahapplewa"
shabd_list = list(shabd)
filtered_shabd=fiterStr(shabd_list,"apple",0,len(shabd_list)-1)
print(filtered_shabd)