def isSorted(index: int, arr: list[int]) -> bool:
    if(index==len(arr)-1):
        return True
    return arr[index]<=arr[index+1] and isSorted(index+1,arr)


def main():
    arr =[0,1,2,99,890]
    print(isSorted(0,arr))
if __name__=="__main__":
    main()