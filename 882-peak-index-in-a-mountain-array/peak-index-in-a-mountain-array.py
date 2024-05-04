class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low, high = 0, len(arr)-1

        while(low<=high):
            mid= int((low+high)/2)
            if(arr[mid-1]>arr[mid]):
                high = mid
            elif(arr[mid+1]>arr[mid]):
                low = mid
            else:
                return mid
        return -1
            

        