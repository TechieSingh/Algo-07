def bubbleSort(arr: list[int], length: int, index: int) -> None:
    if length == 1:
        return
    
    if index<length-1:
        if arr[index] > arr[index + 1]:
            arr[index], arr[index + 1] = arr[index + 1], arr[index]
        bubbleSort(arr,length, index + 1)
    else:
        bubbleSort(arr, length-1,0)

def main():
    arr = [6, 2, 8, 4, 10]
    bubbleSort(arr, len(arr), 0)
    print(arr)

if __name__ == "__main__":
    main()
