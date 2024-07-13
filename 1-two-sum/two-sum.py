class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            val=target-nums[i]
            for j in range(i+1,len(nums)):
                if nums[j]==val:
                    return [i,j]

        return []

        