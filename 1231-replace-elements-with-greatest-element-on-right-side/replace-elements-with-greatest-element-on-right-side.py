class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        left,right=0,len(arr)-1
        result=[-1]
        val_max=0
        while right>left:
            val_max=max(val_max,arr[right])
            result.append(val_max)
            right-=1
        return result[::-1]
            
#[17,18,5,4,6,1]
#l=0, r=3
#[6,4]
#[-1,1,6]
        