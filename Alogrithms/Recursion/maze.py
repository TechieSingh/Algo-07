def path(p:str, r: int, c:int)->int:
    if r==1 and c ==1:
        print(p)
    if r>1:
        path(p+'H',r-1,c)
    if c>1:
        path(p+'V',r,c-1)
    if c>1 and r>1:
        path(p+'D',r-1,c-1)

path("",3,3)