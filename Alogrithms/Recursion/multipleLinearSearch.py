def linearSearch(index: int, arr: list[int],target: int) -> list:
    result=[]
    if index==len(arr):
        return result
    if arr[index]==target:
        result.append(index)
    val=linearSearch(index+1,arr,target)
    result.extend(val)
    return result
    


def main():
    arr =[0,1,2,2,890]
    target=2
    print(linearSearch(0,arr,target))
if __name__=="__main__":
    main()