def linearSearch(index: int, arr: list[int],target: int) -> bool:
    if arr[index]==target:
        return True
    return index<len(arr)-1 and linearSearch(index+1,arr,target)


def main():
    arr =[0,1,2,99,890]
    target=999
    print(linearSearch(0,arr,target))
if __name__=="__main__":
    main()