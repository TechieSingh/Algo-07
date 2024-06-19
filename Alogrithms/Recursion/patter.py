def Pattern(r:int,c:int)-> None:
    if r==0:
        return
    if c<r:
        Pattern(r,c+1)
        print("*",end=" ")
    else:     
        Pattern(r-1,0)
        print("\n")

def main():
    r,c=4,4
    Pattern(r,c)

if __name__=="__main__":
    main()
