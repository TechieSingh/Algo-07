def mergeSort(arr: list, s: int, e: int)-> None:
    if s>=e:
        return
    mid= (s+e)//2
    mergeSort(arr,s,mid)
    mergeSort(arr,mid+1,e)
    merge(arr,s,mid,e)

def merge(arr: list, s: int, mid: int, e: int)-> None:
    left=arr[s:mid+1]
    right=arr[mid+1:e+1]

    i=j=0
    k=s

    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            arr[k]=left[i]
            i+=1
        else:
            arr[k]=right[j]
            j+=1
        k+=1
    while i<len(left):
        arr[k]=left[i]
        i+=1
        k+=1

    while j<len(right):
        arr[k]=right[j]
        j+=1
        k+=1


def main():
    arr=[2,1,7,4,8,3,9]
    mergeSort(arr,0,len(arr))
    print(arr)

if __name__=="__main__":
    main()