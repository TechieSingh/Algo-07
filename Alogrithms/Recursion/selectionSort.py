def selectionSort(arr: list,l: int, i: int)->None:
    if l==0:
        return
    if i<l:
        if arr[i]>arr[l]:
            arr[i],arr[l]=arr[l],arr[i]
        selectionSort(arr,l,i+1)
    else:
        selectionSort(arr,l-1,0)



def main():
    arr=[6,2,8,4,10]
    selectionSort(arr,len(arr)-1,0)
    print(arr)

if __name__=="__main__":
    main()