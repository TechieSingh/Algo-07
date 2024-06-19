def sumof(n: int)-> int:
    if n==0:
        return 0
    return n%10+sumof(n//10)



def main():
    print(sumof(1234))
if __name__=="__main__":
    main()