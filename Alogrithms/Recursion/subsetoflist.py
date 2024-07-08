def sub_set(IGI:list, IGO:list, i:int, j:int, n:int)->None:
    if i>n:
        return 
    elif j<=n:
        IGO.append(''.join(IGI[i:j+1]))
        return sub_set(IGI,IGO,i,j+1,n)
    else:
        return sub_set(IGI,IGO,i+1,i+1,n)



param="abc"
IGI = list(param)
IGO=[]
sub_set(IGI,IGO,0,0,len(IGI)-1)
IGO = list(set(IGO))
print(IGO)

