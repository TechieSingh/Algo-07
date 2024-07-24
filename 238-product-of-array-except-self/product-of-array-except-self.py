class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i=0
        n=len(nums)
        res=[0]*n
        left=1
        for j in range(n):
            res[j]=left
            left*=nums[j]
        
        right=1
        for k in range(n-1,-1,-1):
            res[k]*=right
            right=right*nums[k]
            
        return res

        