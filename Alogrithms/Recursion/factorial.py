def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n*factorial(n - 1)
def main():
    number = 5
    result=factorial(number)
    print(f"The factorial of {number} is {result}")

if __name__ == "__main__":
    main()
