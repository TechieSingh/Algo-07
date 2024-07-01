class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr)<2:
            return False
        n=len(arr)-2
        i=0
        while i<n:
            if arr[i]%2!=0 and arr[i+1]%2!=0 and arr[i+2]%2!=0:
                return True
            else:
                i+=1
        return False    
        