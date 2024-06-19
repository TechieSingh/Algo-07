def reverse(n: int) -> int:
    if n==0:
        return 0
    num_digits = len(str(n)) - 1
    q=pow(10,num_digits)
    return (n%10)*q + reverse(n//10)


def main():
    print(reverse(12345))
if __name__=="__main__":
    main()