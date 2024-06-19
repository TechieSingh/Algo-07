def bubbleSort(arr: list[int], n: int) -> None:
    if n == 1:
        return
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    bubbleSort(arr, n - 1)

def main():
    arr = [6, 2, 8, 4, 10]
    bubbleSort(arr, len(arr))
    print(arr)

if __name__ == "__main__":
    main()
