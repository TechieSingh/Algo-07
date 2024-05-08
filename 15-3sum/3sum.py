class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=[]
        nums.sort()
        for i,a in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left,right=i+1,len(nums)-1
            while left<right:
                total=a+nums[left]+nums[right]
                if total==0:
                    vals=[nums[i], nums[left], nums[right]]
                    result.append(vals)
                    left+=1
                    while nums[left]==nums[left-1] and left<right:
                        left+=1
                elif total>0:
                    right-=1
                else:
                    left+=1
        return result
        