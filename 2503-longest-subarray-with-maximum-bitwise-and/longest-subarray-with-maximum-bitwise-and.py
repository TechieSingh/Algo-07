class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_val= max(nums)
        count=0
        length=0
        for num in nums:
            if num==max_val:
                count+=1
                length= max(length, count)
            else:
                count=0
        return length
        