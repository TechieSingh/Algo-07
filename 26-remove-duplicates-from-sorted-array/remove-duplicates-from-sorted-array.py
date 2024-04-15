class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_index = 0
        for num in nums:
            if num != nums[unique_index]:
                unique_index += 1
                nums[unique_index] = num
        return unique_index + 1
