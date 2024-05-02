class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:  
            return 0  
        val, val_max = nums[0], nums[0]
        for element in nums[1:]:
            val = max(element, val + element)
            val_max = max(val_max, val)

        return val_max